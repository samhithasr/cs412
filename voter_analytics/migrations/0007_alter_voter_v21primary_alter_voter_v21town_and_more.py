# Generated by Django 5.1.2 on 2024-11-10 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter_analytics', '0006_alter_voter_v20state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='v21primary',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='v21town',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='v22general',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='v23town',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='voter_score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
