# Generated by Django 4.1.4 on 2022-12-17 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0012_post_onwhat'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]
