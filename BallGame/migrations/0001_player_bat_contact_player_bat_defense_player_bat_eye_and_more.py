# Generated by Django 4.0.1 on 2022-01-27 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BallGame', '0000_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='bat_contact',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='bat_defense',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='bat_eye',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='bat_power',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='pitch_control',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='pitch_movement',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='pitch_quality',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='pitch_stamina',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='speed',
            field=models.IntegerField(default=0),
        ),
    ]