# Generated by Django 3.2.24 on 2024-05-23 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0030_auto_20220804_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='deviation',
            field=models.IntegerField(default=350),
        ),
        migrations.AddField(
            model_name='submission',
            name='rating',
            field=models.IntegerField(default=400),
        ),
    ]
