# Generated by Django 3.1.7 on 2021-03-09 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0053_remove_automaticperitonealdialysis_additional_drain_ml'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GeneralRecommendation',
            new_name='GeneralRecommendationDeprecated',
        ),
        migrations.RenameModel(
            old_name='GeneralRecommendationCategory',
            new_name='GeneralRecommendationDeprecatedCategory',
        ),
    ]