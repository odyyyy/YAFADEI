# Generated by Django 5.0.3 on 2024-03-10 21:29

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0004_alter_posts_slug_alter_posts_options_posts_img_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posts",
            name="published_time",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 11, 0, 29, 22, 881298),
                verbose_name="Время публикации",
            ),
        ),
    ]
