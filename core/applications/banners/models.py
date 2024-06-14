import os
import uuid

from datetime import date

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver


class ActiveSliderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(Q(end_date__isnull=True) | Q(end_date__gte=date.today()),
                                             start_date__lte=date.today(), is_visible=True, is_delete=False)


def image_validator(image):
    if not image:
        raise ValidationError('Изображение не может быть пустым')

    if isinstance(image, InMemoryUploadedFile):
        image = image.image

    file_resolution = f'{image.width}x{image.height}'
    if file_resolution != settings.BANNER_RESOLUTION:
        raise ValidationError(f'Разрешение изображения должно быть `{settings.BANNER_RESOLUTION} пикселей!`')


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('bn', filename)


class Banner(models.Model):
    name = models.CharField('Кампания (Название)', max_length=150,
                            help_text='Название рекламной кaмпании или акции')
    image = models.ImageField('Изображение', validators=[image_validator, ], upload_to=get_file_path,
                              help_text=f'Размер изображения должен быть {settings.BANNER_RESOLUTION}')
    url = models.URLField('URL перенаправления', blank=True,
                          help_text='URL на который произойдет перенаправление при клике на баннер.')
    start_date = models.DateField('Дата запуска', default=None, help_text='Дата когда начать показ баннера.')
    end_date = models.DateField('Дата завершения', null=True, blank=True,
                                help_text='Дата когда завершить показ баннера.')
    position = models.PositiveSmallIntegerField(default=0, blank=True, null=False)
    is_visible = models.BooleanField('Отображать на сайте', default=True)
    is_delete = models.BooleanField('Удалён', default=False)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата последнего изменения', auto_now=True)

    objects = models.Manager()
    active_sliders = ActiveSliderManager()

    class Meta:
        ordering = ['position']
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.is_delete = True
        self.save(update_fields=['is_delete'])

    @property
    def is_active(self):
        if not self.is_visible:
            return False
        if self.end_date:
            return self.start_date <= date.today() <= self.end_date
        return self.start_date <= date.today()


class BannerStatistics(models.Model):
    banner = models.OneToOneField(Banner, models.CASCADE, verbose_name='Баннер', related_name='statistics')
    count_view = models.PositiveIntegerField('Количество показов', default=0, blank=True)
    count_click = models.PositiveIntegerField('Количество переходов', default=0, blank=True)
    is_delete = models.BooleanField('Удален', default=False)

    class Meta:
        verbose_name = 'Статистика по баннерам'
        verbose_name_plural = 'Статистика по баннерам'

    def __str__(self):
        return self.banner.name

    def delete(self, using=None, keep_parents=False):
        self.is_delete = True
        self.save(update_fields=['is_delete'])


@receiver(post_save, sender=Banner)
def create_banner_statistics(**kwargs):
    if kwargs['created']:
        _, _ = BannerStatistics.objects.get_or_create(banner=kwargs['instance'])
