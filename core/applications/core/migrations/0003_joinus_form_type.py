# Generated by Django 2.1.3 on 2018-12-17 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181215_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='joinus',
            name='form_type',
            field=models.CharField(choices=[('gpon', 'GPON'), ('4g', '4G'), ('smart', 'Smart TV'), ('neo', 'NEO TV')], default='', max_length=50, verbose_name='Тип заявки'),
        ),
    ]