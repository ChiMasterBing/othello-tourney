# Generated by Django 3.2.25 on 2024-05-28 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0013_gauntlet_celery_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gauntlet',
            name='mySide2',
            field=models.CharField(default='x', max_length=1),
        ),
    ]
