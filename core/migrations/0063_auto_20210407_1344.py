# Generated by Django 3.1.7 on 2021-04-07 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0062_auto_20210330_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluserprofile',
            name='dialysis',
            field=models.CharField(choices=[('Unknown', 'Unknown'), ('AutomaticPeritonealDialysis', 'Automaticperitonealdialysis'), ('ManualPeritonealDialysis', 'Manualperitonealdialysis'), ('Hemodialysis', 'Hemodialysis'), ('PostTransplant', 'Posttransplant'), ('NotPerformed', 'Notperformed')], default='Unknown', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='dialysis',
            field=models.CharField(choices=[('Unknown', 'Unknown'), ('AutomaticPeritonealDialysis', 'Automaticperitonealdialysis'), ('ManualPeritonealDialysis', 'Manualperitonealdialysis'), ('Hemodialysis', 'Hemodialysis'), ('PostTransplant', 'Posttransplant'), ('NotPerformed', 'Notperformed')], default='Unknown', max_length=32),
            preserve_default=False,
        ),
    ]