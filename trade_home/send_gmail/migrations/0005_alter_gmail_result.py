# Generated by Django 4.2.1 on 2023-08-09 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_gmail', '0004_alter_gmail_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gmail',
            name='result',
            field=models.CharField(choices=[('None', ' '), ('True', '通過'), ('False', '不通過')], default=None, max_length=10000, verbose_name='解果'),
        ),
    ]
