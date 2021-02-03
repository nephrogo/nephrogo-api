# Generated by Django 3.1.6 on 2021-02-03 14:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20210203_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluserprofile',
            name='year_of_birth',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1920), django.core.validators.MaxValueValidator(2003)]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='year_of_birth',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1920), django.core.validators.MaxValueValidator(2003)]),
        ),
    ]
