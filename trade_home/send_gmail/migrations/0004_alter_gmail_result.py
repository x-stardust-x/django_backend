# Generated by Django 4.2.1 on 2023-08-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_gmail', '0003_alter_gmail_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gmail',
            name='result',
            field=models.CharField(choices=[(True, '通過'), (False, '不通過')], default=None, max_length=10000, verbose_name='解果'),
        ),
    ]
