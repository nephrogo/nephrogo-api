# Generated by Django 3.1.6 on 2021-02-04 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20210203_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_marketing_allowed',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
