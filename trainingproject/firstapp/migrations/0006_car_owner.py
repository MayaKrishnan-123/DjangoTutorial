# Generated by Django 2.2.4 on 2019-08-12 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20190807_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
