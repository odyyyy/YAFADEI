# Generated by Django 5.0.3 on 2024-03-13 16:23

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0008_alter_posts_published_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posts",
            name="published_time",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 13, 19, 23, 43, 237472),
                verbose_name="Время публикации",
            ),
        ),
    ]
