# Generated by Django 2.1.3 on 2018-12-23 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_joinus_form_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='callme',
            name='user',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Оператор принявший заявку'),
        ),
        migrations.AddField(
            model_name='joinus',
            name='user',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Оператор принявший заявку'),
        ),
        migrations.AlterField(
            model_name='callme',
            name='status',
            field=models.CharField(choices=[('new', 'Новая заявка'), ('accepted', 'Принятая заявка')], default='new', max_length=50, verbose_name='Статус звонка'),
        ),
    ]
