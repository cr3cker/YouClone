# Generated by Django 4.1.2 on 2022-12-03 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_hosting', '0013_alter_video_dislikes_percentage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='dislikes_percentage',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='video',
            name='views',
            field=models.IntegerField(default=410324),
        ),
    ]