# Generated by Django 4.1.7 on 2023-03-23 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catapp', '0003_remove_user_name_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
