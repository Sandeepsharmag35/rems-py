# Generated by Django 4.2.1 on 2023-05-29 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_uploadedimage_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SellRequest',
        ),
        migrations.DeleteModel(
            name='UploadedImage',
        ),
    ]
