# Generated by Django 4.2.1 on 2023-05-31 02:19

import app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_alter_property_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(blank=True, upload_to='property_images', validators=[app.validators.image_validations]),
        ),
    ]
