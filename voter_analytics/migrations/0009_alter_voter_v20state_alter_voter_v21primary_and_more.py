# Generated by Django 5.1.2 on 2024-11-10 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter_analytics', '0008_alter_voter_v20state_alter_voter_v21primary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='v20state',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='voter',
            name='v21primary',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='voter',
            name='v21town',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='voter',
            name='v22general',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='voter',
            name='v23town',
            field=models.BooleanField(default=False),
        ),
    ]
