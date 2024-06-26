# Generated by Django 3.2.25 on 2024-05-25 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import othello.apps.games.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0032_submission_gauntlet'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gauntlet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('game_time_limit', models.IntegerField(default=5, validators=[othello.apps.games.validators.validate_game_time_limit])),
                ('running', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
                ('terminated', models.BooleanField(default=False)),
                ('submission', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='gauntletsubmission', to='games.submission')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
