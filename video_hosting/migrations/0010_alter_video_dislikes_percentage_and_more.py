# Generated by Django 4.1.2 on 2022-12-03 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_hosting', '0009_alter_video_dislikes_percentage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='dislikes_percentage',
            field=models.IntegerField(default=8),
        ),
        migrations.AlterField(
            model_name='video',
            name='likes_percentage',
            field=models.IntegerField(default=83),
        ),
        migrations.AlterField(
            model_name='video',
            name='views',
            field=models.IntegerField(default=386560),
        ),
    ]