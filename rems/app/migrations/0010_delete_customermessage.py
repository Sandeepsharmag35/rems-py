# Generated by Django 4.1.7 on 2023-05-10 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_customermessage_property'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomerMessage',
        ),
    ]