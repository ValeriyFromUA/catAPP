# Generated by Django 4.1.7 on 2023-03-30 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catapp", "0013_remove_posts_tags_remove_posttags_tag_posttags_name_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="posttags",
            old_name="name",
            new_name="tag",
        ),
    ]
