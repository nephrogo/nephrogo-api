# Generated by Django 3.1.7 on 2021-03-05 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_auto_20210304_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='automaticperitonealdialysis',
            name='additional_drain_ml',
        ),
    ]