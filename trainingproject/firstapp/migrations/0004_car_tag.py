# Generated by Django 2.2.4 on 2019-08-07 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='tag',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
