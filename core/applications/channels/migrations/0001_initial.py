# Generated by Django 2.1.3 on 2018-12-16 12:19

import applications.channels.models
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название канала')),
                ('slug', models.SlugField(max_length=100, verbose_name='Слаг канала')),
                ('image', models.ImageField(upload_to=applications.channels.models.get_file_path, verbose_name='Изображение канала')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание канала')),
                ('position', models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Позиция в списке')),
            ],
            options={
                'verbose_name': 'канал',
                'verbose_name_plural': 'каналы',
                'ordering': ['position'],
            },
        ),
    ]