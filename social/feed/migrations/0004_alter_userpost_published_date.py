# Generated by Django 4.1.5 on 2023-01-30 14:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_userpost_user_profile_alter_userpost_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 30, 16, 34, 19, 473791)),
        ),
    ]
