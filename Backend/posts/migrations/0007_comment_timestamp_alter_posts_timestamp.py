# Generated by Django 4.1 on 2022-10-01 10:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_posts_timestamp_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 1, 16, 5, 11, 874828)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 1, 16, 5, 11, 874828)),
        ),
    ]
