# Generated by Django 4.1.4 on 2022-12-17 19:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0013_thread_closed'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likedby',
            field=models.ManyToManyField(blank=True, related_name='likedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
