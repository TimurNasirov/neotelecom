# Generated by Django 2.1.3 on 2018-12-16 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0002_auto_20181215_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='end_date',
            field=models.DateField(blank=True, help_text='Дата когда завершить показ баннера.', null=True, verbose_name='Дата завершения'),
        ),
    ]
