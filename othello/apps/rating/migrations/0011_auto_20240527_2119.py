# Generated by Django 3.2.25 on 2024-05-28 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0010_alter_gauntlet_myside3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gauntlet',
            name='mySide1',
            field=models.CharField(default='x', max_length=1),
        ),
        migrations.AlterField(
            model_name='gauntlet',
            name='mySide2',
            field=models.CharField(default='o', max_length=1),
        ),
        migrations.AlterField(
            model_name='gauntlet',
            name='mySide3',
            field=models.CharField(default='o', max_length=1),
        ),
        migrations.AlterField(
            model_name='rankedmanager',
            name='next_auto_run',
            field=models.DateTimeField(),
        ),
    ]
