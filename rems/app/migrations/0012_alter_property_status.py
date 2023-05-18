# Generated by Django 4.2.1 on 2023-05-18 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_customermessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='status',
            field=models.CharField(choices=[('select', 'Select'), ('available', 'Available'), ('rented', 'Rented'), ('sold', 'Sold')], default='select', max_length=20),
        ),
    ]
