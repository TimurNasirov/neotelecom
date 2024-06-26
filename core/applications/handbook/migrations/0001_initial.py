# Generated by Django 2.1.3 on 2018-12-16 10:40

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HandBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('smart_tv', 'Smart TV'), ('neo_tv', 'NEO TV'), ('gpon', 'GPON интернет'), ('4g', '4G интернет'), ('about_us', 'О нас')], max_length=50, verbose_name='Категория')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Информация')),
            ],
            options={
                'verbose_name': 'справочник',
                'verbose_name_plural': 'справочник',
            },
        ),
    ]
