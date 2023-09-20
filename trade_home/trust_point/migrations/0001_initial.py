# Generated by Django 4.2.1 on 2023-09-13 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='matchmaking',
            fields=[
                ('id', models.CharField(max_length=10000, primary_key=True, serialize=False, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='trust_point',
            fields=[
                ('trust_point', models.PositiveIntegerField(default=100, max_length=100, verbose_name='信用積分')),
                ('id', models.CharField(max_length=10000, primary_key=True, serialize=False, verbose_name='email')),
            ],
        ),
    ]
