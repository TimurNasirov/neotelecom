# Generated by Django 2.1.3 on 2018-12-15 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('phone', models.CharField(max_length=100, verbose_name='Номер телефона')),
                ('status', models.CharField(choices=[('new', 'Новый звонок'), ('acepted', 'Обработаный звонок')], default='new', max_length=50, verbose_name='Статус звонка')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата поступления')),
            ],
            options={
                'verbose_name': 'Звонок',
                'verbose_name_plural': 'Звонки',
                'ordering': ['created_at'],
            },
        ),
        migrations.AlterField(
            model_name='joinus',
            name='status',
            field=models.CharField(choices=[('new', 'Новая заявка'), ('accepted', 'Принятая заявка')], default='new', max_length=50, verbose_name='Статус заявки'),
        ),
    ]