# Generated by Django 3.1.6 on 2021-02-18 16:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20210218_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pulse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pulse', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(200)])),
                ('measured_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('daily_health_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pulses', to='core.dailyhealthstatus')),
            ],
        ),
        migrations.AddConstraint(
            model_name='pulse',
            constraint=models.UniqueConstraint(fields=('daily_health_status', 'measured_at'), name='unique_pulse_health_status_measure_at'),
        ),
    ]
