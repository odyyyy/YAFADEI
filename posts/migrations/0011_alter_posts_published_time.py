# Generated by Django 5.0.3 on 2024-03-13 16:50

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0010_alter_posts_published_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posts",
            name="published_time",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 13, 19, 50, 25, 771483),
                verbose_name="Время публикации",
            ),
        ),
    ]