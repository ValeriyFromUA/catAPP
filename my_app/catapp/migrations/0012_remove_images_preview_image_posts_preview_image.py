# Generated by Django 4.1.7 on 2023-03-29 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catapp', '0011_images_preview_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='preview_image',
        ),
        migrations.AddField(
            model_name='posts',
            name='preview_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
