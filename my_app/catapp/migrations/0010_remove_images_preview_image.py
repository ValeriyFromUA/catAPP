# Generated by Django 4.1.7 on 2023-03-28 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catapp", "0009_alter_images_image_alter_images_preview_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="images",
            name="preview_image",
        ),
    ]
