# Generated by Django 2.1.3 on 2018-12-15 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map_type', models.CharField(choices=[('4g', '4G'), ('gpon', 'GPON'), ('smart_tv', 'Smart TV')], max_length=20, verbose_name='Тип карты')),
                ('name', models.CharField(max_length=100, verbose_name='Название зоны')),
                ('coordinates', models.TextField(help_text='Вводятся координаты в формате *долгота,широта долгота,широта* и т.д.', verbose_name='Координаты краёв зоны')),
            ],
            options={
                'verbose_name': 'Карта',
                'verbose_name_plural': 'Карты',
                'ordering': ['map_type'],
            },
        ),
    ]
