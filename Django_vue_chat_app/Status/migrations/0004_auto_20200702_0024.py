# Generated by Django 2.1.7 on 2020-07-01 23:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Status', '0003_auto_20200701_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='messages',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 2, 0, 24, 56, 619083)),
        ),
    ]
