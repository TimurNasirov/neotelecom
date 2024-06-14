import os
import uuid

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from applications.core.models import City
from applications.core.utils import ProductionManager

PRICE_TYPE_CHOICE = (
    (0, 'сом/сутки'),
    (1, 'сом/неделю'),
    (2, 'сом/месяц'),
    (3, 'сом'),
)


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('promos', filename)


class Promotion(models.Model):
    title = models.CharField('Заголовок', max_length=150)
    sub_title = models.CharField('Подзаголовок', max_length=150)
    description = RichTextUploadingField('Описание', max_length=500)

    image = models.ImageField('Изображение', upload_to=get_file_path)

    bullet_one = models.CharField('1-й буллет', max_length=50, blank=True, default='')
    bullet_two = models.CharField('2-й буллет', max_length=50, blank=True, default='')
    bullet_three = models.CharField('3-й буллет', max_length=50, blank=True, default='')

    price = models.PositiveSmallIntegerField('Цена')
    price_type = models.IntegerField('Тип цены', choices=PRICE_TYPE_CHOICE, default=0)

    city = models.ManyToManyField(City, verbose_name='Города',
                                  help_text='Список городов на которые распространяется акция')

    start_date = models.DateField('Дата запуска', help_text='Дата когда начать показ акции.')
    end_date = models.DateField('Дата завершения', help_text='Дата когда завершить показ акции.')

    is_visible = models.BooleanField('Отображать на сайте', default=True)
    is_delete = models.BooleanField('Удалена', default=False)

    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата последнего изменения', auto_now=True)

    objects = models.Manager()
    production = ProductionManager()

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return self.title

