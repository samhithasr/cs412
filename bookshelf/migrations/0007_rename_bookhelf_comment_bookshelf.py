# Generated by Django 5.1.3 on 2024-11-30 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0006_comment_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='bookhelf',
            new_name='bookshelf',
        ),
    ]
