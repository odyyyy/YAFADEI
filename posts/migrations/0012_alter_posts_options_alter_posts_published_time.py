# Generated by Django 5.0.3 on 2024-03-17 20:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0011_alter_posts_published_time"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="posts",
            options={
                "ordering": ["-published_time"],
                "verbose_name": "Посты",
                "verbose_name_plural": "Посты",
            },
        ),
        migrations.AlterField(
            model_name="posts",
            name="published_time",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                verbose_name="Время публикации",
            ),
        ),
    ]
