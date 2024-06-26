# Generated by Django 2.1.3 on 2018-12-26 11:32

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0003_promotion_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='bullet_one',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='1-й буллет'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='bullet_three',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='3-й буллет'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='bullet_two',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='2-й буллет'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=500, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='price_type',
            field=models.IntegerField(choices=[(0, 'сом/сутки'), (1, 'сом/неделю'), (2, 'сом/месяц'), (3, 'сом')], default=0, verbose_name='Тип цены'),
        ),
    ]
