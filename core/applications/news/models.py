from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class News(models.Model):

    NEWS_TYPE_CHOICES = (
        ('tech', 'Технические новости'),
        ('media', 'Медиа'),
    )

    news_type = models.CharField('Тип', max_length=20, choices=NEWS_TYPE_CHOICES, default='company')
    title = models.CharField('Заголовок', max_length=80)
    body = RichTextUploadingField('Тело сообщения')

    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
