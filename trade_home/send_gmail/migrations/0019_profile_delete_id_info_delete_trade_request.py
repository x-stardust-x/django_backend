# Generated by Django 4.2.5 on 2023-10-04 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('send_gmail', '0018_trade_request_description_limit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jwt_token', models.CharField(max_length=400)),
                ('description', models.CharField(blank=True, default=None, max_length=400, null=True)),
                ('obj_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='id_info',
        ),
        migrations.DeleteModel(
            name='trade_request',
        ),
    ]
