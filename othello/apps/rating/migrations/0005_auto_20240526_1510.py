# Generated by Django 3.2.25 on 2024-05-26 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0004_alter_gauntlet_myside1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gauntlet',
            name='mySide1',
            field=models.CharField(default='o', max_length=1),
        ),
        migrations.AlterField(
            model_name='gauntlet',
            name='mySide2',
            field=models.CharField(default='x', max_length=1),
        ),
        migrations.AlterField(
            model_name='gauntlet',
            name='mySide3',
            field=models.CharField(default='x', max_length=1),
        ),
    ]
