# Generated by Django 5.0.3 on 2024-03-10 15:32

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок поста')),
                ('img', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('karma', models.IntegerField(default=0, verbose_name='Карма')),
                ('published_time', models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', tinymce.models.HTMLField()),
                ('slug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.postcards')),
            ],
        ),
    ]
