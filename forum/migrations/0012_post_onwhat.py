# Generated by Django 4.1.4 on 2022-12-16 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0011_thread_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='onwhat',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='forum.thread'),
            preserve_default=False,
        ),
    ]