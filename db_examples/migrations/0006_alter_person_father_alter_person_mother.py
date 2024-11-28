# Generated by Django 5.1.3 on 2024-11-19 16:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_examples', '0005_alter_registration_grade_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='father',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='father_person', to='db_examples.person'),
        ),
        migrations.AlterField(
            model_name='person',
            name='mother',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mother_person', to='db_examples.person'),
        ),
    ]