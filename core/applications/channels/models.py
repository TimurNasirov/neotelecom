import os
import uuid

from ckeditor.fields import RichTextField
from django.db import models


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('channels', filename)


class Channel(models.Model):
    title = models.CharField('Название канала', max_length=100)
    slug = models.SlugField('Слаг канала', max_length=100)

    image = models.ImageField('Изображение канала', upload_to=get_file_path)
    description = RichTextField('Описание канала')

    position = models.PositiveSmallIntegerField('Позиция в списке', default=0, blank=True, null=False)

    class Meta:
        ordering = ['position']
        verbose_name = 'канал'
        verbose_name_plural = 'каналы'

    def __str__(self):
        return self.title
