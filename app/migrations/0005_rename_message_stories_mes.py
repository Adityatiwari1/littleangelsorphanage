# Generated by Django 3.2.3 on 2021-11-17 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_stories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stories',
            old_name='message',
            new_name='mes',
        ),
    ]
