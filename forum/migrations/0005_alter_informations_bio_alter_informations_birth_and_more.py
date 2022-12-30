# Generated by Django 4.1.3 on 2022-12-15 21:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_informations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informations',
            name='bio',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='informations',
            name='birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='informations',
            name='gender',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='informations',
            name='image',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='informations',
            name='who',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]