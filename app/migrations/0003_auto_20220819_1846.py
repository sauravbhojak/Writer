# Generated by Django 3.2.15 on 2022-08-19 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_created',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_updated',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_verified',
        ),
    ]