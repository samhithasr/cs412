# Generated by Django 5.1.3 on 2024-11-19 16:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_examples', '0003_course_students_student_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateField(auto_now_add=True)),
                ('grade', models.CharField(max_length=2)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_examples.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_examples.student')),
            ],
        ),
    ]
