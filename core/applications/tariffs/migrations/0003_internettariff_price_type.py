# Generated by Django 2.1.3 on 2018-12-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tariffs', '0002_internettariff_tech_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='internettariff',
            name='price_type',
            field=models.IntegerField(choices=[(0, 'сом/сут.'), (1, 'сом/нед.'), (2, 'сом/мес.')], default=2, verbose_name='Тип цены'),
        ),
    ]
