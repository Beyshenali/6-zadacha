# Generated by Django 5.0.1 on 2024-01-24 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_delete_blok_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blok_Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовок блока')),
                ('title1', models.CharField(max_length=155, verbose_name='Заголовок Текста')),
                ('description1', models.TextField(verbose_name='Описание первого текста')),
                ('title2', models.CharField(max_length=155, verbose_name='Заголовок второго текста')),
                ('description2', models.TextField(verbose_name='Описание второго текста')),
                ('title3', models.CharField(max_length=155, verbose_name='Заголовок третего текста')),
                ('description3', models.TextField(verbose_name='Описание третего текста')),
                ('link', models.URLField(verbose_name='Ссылка для Портфоля')),
                ('image', models.ImageField(upload_to='portrait/', verbose_name='Фотография блока')),
            ],
        ),
    ]
