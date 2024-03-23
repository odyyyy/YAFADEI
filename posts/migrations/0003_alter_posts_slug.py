# Generated by Django 5.0.3 on 2024-03-10 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_alter_postcards_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posts",
            name="slug",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="posts.postcards",
            ),
        ),
    ]
