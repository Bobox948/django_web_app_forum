# Generated by Django 4.1.3 on 2022-12-15 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]
