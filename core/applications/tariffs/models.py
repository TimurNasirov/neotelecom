from django.db import models

from applications.core.models import City

PRICE_TYPE_CHOICE = (
        (0, 'сом/сут.'),
        (1, 'сом/нед.'),
        (2, 'сом/мес.'),
    )


class InternetTariff(models.Model):
    TECH_TYPE_CHOICES = (
        ('gpon', 'GPON'),
        ('4g', '4G'),
    )

    name = models.CharField('Название тарифа', max_length=50)
    speed = models.PositiveSmallIntegerField('Скорость ДО Мбит/сек')
    price = models.PositiveIntegerField('Абонентская плата')
    price_type = models.IntegerField('Тип цены', choices=PRICE_TYPE_CHOICE, default=2)
    extra_neo_tv = models.PositiveSmallIntegerField('Количество точек NeoTv', default=0, blank=True)
    extra_smart_tv = models.PositiveSmallIntegerField('Количество точек SmartTv', default=0, blank=True)

    city = models.ManyToManyField(City, verbose_name='Города',
                                  help_text='Список городов на которые распространяется данный тариф')

    tech_type = models.CharField('Технология', max_length=50, choices=TECH_TYPE_CHOICES, blank=True, null=True)
    position = models.PositiveSmallIntegerField(default=0, blank=True, null=False)

    class Meta:
        ordering = ['position']
        verbose_name = 'Интернет тариф'
        verbose_name_plural = 'Интернет тарифы'

    def __str__(self):
        return self.name

    def get_price(self):
        return f'{self.price} {self.get_price_type_display()}'


class TvTariff(models.Model):
    TECH_TYPE_CHOICES = (
        ('smart_tv', 'Smart TV'),
        ('neo_tv', 'NEO TV'),
    )

    name = models.CharField('Название тарифа', max_length=50)
    channels_count = models.PositiveSmallIntegerField('Количество телеканалов')
    price = models.PositiveIntegerField('Абонентская плата')
    price_type = models.IntegerField('Тип цены', choices=PRICE_TYPE_CHOICE, default=2)
    city = models.ManyToManyField(City, verbose_name='Города',
                                  help_text='Список городов на которые распространяется данный тариф')

    extra_package = models.BooleanField('Дополнительный пакет', default=False)
    tech_type = models.CharField('Технология', max_length=50, choices=TECH_TYPE_CHOICES, blank=True, null=True)
    position = models.PositiveSmallIntegerField(default=0, blank=True, null=False)

    objects = models.Manager()

    class Meta:
        ordering = ['position']
        verbose_name = 'Тариф TV'
        verbose_name_plural = 'Тарифы TV'

    def __str__(self):
        return self.name

    def get_price(self):
        return f'{self.price} {self.get_price_type_display()}'

    def get_channels_count(self):
        if self.extra_package:
            return f'Около {self.channels_count} каналов к основному пакету'
        return f'Более {self.channels_count} каналов'
