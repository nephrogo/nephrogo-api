# Generated by Django 3.1.7 on 2021-04-07 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0063_auto_20210407_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluserprofile',
            name='diabetes_time',
            field=models.CharField(choices=[('Unknown', 'Unknown'), ('<1', 'Belowone'), ('2-5', 'Twotofive'), ('6-10', 'Sixtoten'), ('>10', 'Morethanten')], default='Unknown', max_length=16),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='diabetes_time',
            field=models.CharField(choices=[('Unknown', 'Unknown'), ('<1', 'Belowone'), ('2-5', 'Twotofive'), ('6-10', 'Sixtoten'), ('>10', 'Morethanten')], default='Unknown', max_length=16),
        ),
        migrations.AlterField(
            model_name='historicaluserprofile',
            name='dialysis',
            field=models.CharField(choices=[('Unknown', 'Unknown'), ('AutomaticPeritonealDialysis', 'Automaticperitonealdialysis'), ('ManualPeritonealDialysis', 'Manualperitonealdialysis'), ('Hemodialysis', 'Hemodialysis'), ('PostTransplant', 'Posttransplant'), ('NotPerformed', 'Notperformed')], default='Unknown', max_length=32),
        ),
        migrations.AlterField(
            model_name='historicaluserprofile',
            name='dialysis_type',
            field=models.CharField(choices=[('Unknown', 'Unknown'), ('PeriotonicDialysis', 'Periotonicdialysis'), ('Hemodialysis', 'Hemodialysis'), ('PostTransplant', 'Posttransplant'), ('NotPerformed', 'Notperformed')], default='Unknown', max_length=32),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dialysis',
            field=models.CharField(choices=[('Unknown', 'Unknown'), ('AutomaticPeritonealDialysis', 'Automaticperitonealdialysis'), ('ManualPeritonealDialysis', 'Manualperitonealdialysis'), ('Hemodialysis', 'Hemodialysis'), ('PostTransplant', 'Posttransplant'), ('NotPerformed', 'Notperformed')], default='Unknown', max_length=32),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dialysis_type',
            field=models.CharField(choices=[('Unknown', 'Unknown'), ('PeriotonicDialysis', 'Periotonicdialysis'), ('Hemodialysis', 'Hemodialysis'), ('PostTransplant', 'Posttransplant'), ('NotPerformed', 'Notperformed')], default='Unknown', max_length=32),
        ),
    ]
