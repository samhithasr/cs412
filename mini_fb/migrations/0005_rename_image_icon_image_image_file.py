# Generated by Django 5.1.2 on 2024-10-18 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0004_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image_icon',
            new_name='image_file',
        ),
    ]
