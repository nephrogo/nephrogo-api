# Generated by Django 3.1.6 on 2021-02-16 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20210216_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyintakesreport',
            name='daily_norm_carbohydrates_mg',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dailyintakesreport',
            name='daily_norm_fat_mg',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
