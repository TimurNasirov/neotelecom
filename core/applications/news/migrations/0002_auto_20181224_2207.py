# Generated by Django 2.1.3 on 2018-12-24 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_type',
            field=models.CharField(choices=[('tech', 'Технические новости'), ('media', 'Медиа')], default='company', max_length=20, verbose_name='Тип'),
        ),
    ]
