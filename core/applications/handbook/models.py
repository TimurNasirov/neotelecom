from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class HandBook(models.Model):
    CATEGORY_CHOICES = (
        ('smart_tv', 'Smart TV'),
        ('neo_tv', 'NEO TV'),
        ('gpon', 'GPON интернет'),
        ('4g', '4G интернет'),
        ('about_us', 'О нас'),
    )

    category = models.CharField('Категория', max_length=50, choices=CATEGORY_CHOICES)
    title = models.CharField('Заголовок', max_length=255)
    position = models.PositiveIntegerField('Позиция в спике', default=0, blank=True, null=False)
    description = RichTextUploadingField('Информация')

    class Meta:
        ordering = ['position']
        verbose_name = 'справочник'
        verbose_name_plural = 'справочник'

    def __str__(self):
        return self.title
