# Generated by Django 5.1.3 on 2024-12-10 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0007_rename_bookhelf_comment_bookshelf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='icon',
            field=models.URLField(blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='shelves',
            unique_together={('book', 'shelf')},
        ),
    ]
