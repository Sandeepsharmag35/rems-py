# Generated by Django 4.2.1 on 2023-06-15 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile_profile_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_pic',
            new_name='profile_picture',
        ),
    ]
