# Generated by Django 4.1.7 on 2023-03-30 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catapp", "0012_remove_images_preview_image_posts_preview_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="posts",
            name="tags",
        ),
        migrations.RemoveField(
            model_name="posttags",
            name="tag",
        ),
        migrations.AddField(
            model_name="posttags",
            name="name",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.DeleteModel(
            name="Tags",
        ),
    ]
