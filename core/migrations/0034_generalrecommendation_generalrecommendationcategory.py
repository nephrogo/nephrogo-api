# Generated by Django 3.1.6 on 2021-02-16 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_auto_20210213_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralRecommendationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_lt', models.CharField(max_length=128)),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('order', 'pk'),
            },
        ),
        migrations.CreateModel(
            name='GeneralRecommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_lt', models.CharField(max_length=256)),
                ('answer_lt', models.TextField()),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='questions', to='core.generalrecommendationcategory')),
            ],
        ),
    ]
