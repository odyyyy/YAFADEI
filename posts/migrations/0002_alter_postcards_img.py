# Generated by Django 5.0.3 on 2024-03-10 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcards',
            name='img',
            field=models.ImageField(default='media/svg/no_image_avaliable.svg', upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
