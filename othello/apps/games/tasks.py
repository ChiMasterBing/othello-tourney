from celery import shared_task
from django.conf import settings
from asgiref.sync import async_to_sync
from celery.utils.log import get_task_logger
from channels.layers import get_channel_layer

from ..games.models import Game, Player
from ...moderator import *

task_logger = get_task_logger(__name__)


def send_through_socket(game, event_type):
    task_logger.error(f"sending {event_type}")
    async_to_sync(get_channel_layer().group_send)(
        game.channels_group_name, {"type": event_type}
    )


@shared_task
def run_game(game_id):
    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        return

    mod, time_limit = Moderator(), game.time_limit
    game_over = False

    with PlayerRunner(game.black.code.path, settings.JAILEDRUNNER_DRIVER, settings.DEBUG) as player_black:
        with PlayerRunner(game.white.code.path, settings.JAILEDRUNNER_DRIVER, settings.DEBUG) as player_white:

            game.moves.create(
                board=INITIAL_BOARD,
                player="-",
                possible=[26, 19, 44, 37]
            )
            send_through_socket(game, "game.update")

            while not mod.is_game_over():
                board, current_player = mod.get_game_state()

                try:
                    if current_player == Player.BLACK:
                        running_turn = player_black.get_move(board, current_player.value, time_limit)
                    elif current_player == Player.WHITE:
                        running_turn = player_white.get_move(board, current_player.value, time_limit)
                except BaseException as e:
                    task_logger.error(str(e))

                for log in running_turn:
                    game.logs.create(
                        player=current_player.value,
                        message=log,
                    )
                    send_through_socket(game, "game.log")
                submitted_move, error = running_turn.return_value

                if error != 0:
                    game.errors.create(
                        player=current_player.value,
                        error_code=error.value[0],
                        error_msg=error.value[1],
                    )
                    if isinstance(error, ServerError):
                        game.forfeit = False
                        game.outcome = 'T'
                    elif isinstance(error, UserError):
                        game.forfeit = True
                        game.outcome = Player.BLACK.value if current_player == Player.WHITE else Player.WHITE.value
                    game.playing = False
                    game.save(update_fields=["forfeit", "outcome", "playing"])
                    send_through_socket(game, "game.error")
                    break

                try:
                    if submitted := mod.submit_move(submitted_move):
                        flipped, possible = submitted
                    else:
                        game_over = True
                except InvalidMoveError as e:
                    game.errors.create(
                        player=current_player.value,
                        error_code=e.code,
                        error_msg=e.message,
                    )
                    game.forfeit, game.playing = True, False
                    game.outcome = Player.BLACK.value if current_player == Player.WHITE else Player.WHITE.value
                    game.save(update_fields=["forfeit", "outcome", "playing"])
                    send_through_socket(game, "game.error")
                    break

                game.moves.create(
                    player=current_player.value,
                    move=submitted_move,
                    board=mod.get_board(),
                    flipped=flipped,
                    possible=possible
                )
                if game_over:
                    game.forfeit, game.playing = False, False
                    game.outcome = mod.outcome()
                    game.save(update_fields=["forfeit", "outcome", "playing"])
                    task_logger.error("GAME OVER")
                    break
                send_through_socket(game, "game.update")

    game.playing = False
    game.save(update_fields=["playing"])
    game.delete()