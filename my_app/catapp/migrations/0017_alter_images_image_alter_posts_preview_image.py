# Generated by Django 4.1.7 on 2023-04-03 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catapp', '0016_alter_images_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='posts/<built-in function id>/'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='preview_image',
            field=models.ImageField(blank=True, upload_to='posts/preview/<built-in function id>/'),
        ),
    ]