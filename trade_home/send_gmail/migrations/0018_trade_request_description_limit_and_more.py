# Generated by Django 4.2.1 on 2023-09-27 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_gmail', '0017_trade_request_people_limit_trade_request_point_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade_request',
            name='description_limit',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='專長限制'),
        ),
        migrations.AddField(
            model_name='trade_request',
            name='thumbnail',
            field=models.TextField(blank=True, verbose_name='圖片路徑'),
        ),
    ]