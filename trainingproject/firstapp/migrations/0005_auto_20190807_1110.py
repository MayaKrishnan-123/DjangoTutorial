# Generated by Django 2.2.4 on 2019-08-07 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_car_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Thenga', 'verbose_name_plural': 'Something'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
    ]
