# Generated by Django 2.1.3 on 2018-12-17 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181215_2205'),
        ('tariffs', '0004_auto_20181216_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='internettariff',
            name='city',
            field=models.ManyToManyField(help_text='Список городов на которые распространяется данный тариф', to='core.City', verbose_name='Города'),
        ),
    ]
