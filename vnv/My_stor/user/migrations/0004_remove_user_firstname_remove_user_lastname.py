# Generated by Django 4.1.7 on 2023-02-28 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_lastname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastname',
        ),
    ]
