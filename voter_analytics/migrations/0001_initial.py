# Generated by Django 5.1.2 on 2024-11-10 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last', models.TextField()),
                ('first', models.TextField()),
                ('adNumber', models.IntegerField()),
                ('street', models.TextField()),
                ('aptNum', models.CharField(blank=True, max_length=6, null=True)),
                ('zipCode', models.IntegerField()),
                ('dob', models.DateField()),
                ('dor', models.DateField()),
                ('party', models.CharField(max_length=2)),
                ('precint', models.IntegerField()),
                ('voter_score', models.IntegerField()),
            ],
        ),
    ]
