# Generated by Django 3.0.5 on 2020-04-17 07:04

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0013_move'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='move',
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
