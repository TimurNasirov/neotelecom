from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

STATUS_CHOICES = (
    ('new', 'Новая заявка'),
    ('accepted', 'Принятая заявка'),
)


class City(models.Model):
    title = models.CharField('Город', max_length=200)
    slug = models.SlugField('Слаг города', max_length=50, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'

    def __str__(self):
        return self.title


class JoinUs(models.Model):
    OWNERSHIP_CHOICES = (
        ('fiz', 'Физическе лицо'),
        ('yur', 'Юридическое лицо'),
    )

    FORM_TYPE_CHOICES = (
        ('gpon', 'GPON'),
        ('4g', '4G'),
        ('smart', 'Smart TV'),
        ('neo', 'NEO TV'),
    )

    form_type = models.CharField('Тип заявки', max_length=50, choices=FORM_TYPE_CHOICES, default='')
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Номер телефона', max_length=100)
    address = models.CharField('Адрес', max_length=150)
    ownership = models.CharField('Форма собственности', max_length=50, choices=OWNERSHIP_CHOICES, default='')

    user = models.CharField('Оператор принявший заявку', max_length=255, blank=True, default='')
    status = models.CharField('Статус заявки', max_length=50, choices=STATUS_CHOICES, default='new')

    created_at = models.DateTimeField('Дата поступления', auto_now_add=True)

    class Meta: 
        ordering = ['-created_at']
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'

    def __str__(self):
        return f'{self.name} - {self.phone}'


class CallMe(models.Model):
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Номер телефона', max_length=100)

    user = models.CharField('Оператор принявший заявку', max_length=255, blank=True, default='')
    status = models.CharField('Статус звонка', max_length=50, choices=STATUS_CHOICES, default='new')

    created_at = models.DateTimeField('Дата поступления', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'звонок'
        verbose_name_plural = 'звонки'

    def __str__(self):
        return f'{self.name} - {self.phone}'


class Vacancy(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    short_description = models.CharField('Краткое описание', max_length=250,
                                         help_text='Краткий текст в списке вакансий для вовлечения соискателей.')
    description = RichTextUploadingField('Описание')

    created_at = models.DateField('Дата создания', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'

    def __str__(self):
        return self.title


class NeoTvFiles(models.Model):
    MOBILE_FILE_TYPE_CHOICES = (
        ('win', 'Windows'),
        ('macos', 'Mac OS'),
        ('armv7', 'Android arm v7'),
        ('armx64', 'Android arm x64'),
        ('armx86', 'Android arm x86'),
        ('youtube', 'YouTube плеер'),
    )
    type = models.CharField('Тип файла', max_length=50, unique=True, choices=MOBILE_FILE_TYPE_CHOICES)
    url = models.FileField('Файл для загрузки', upload_to='neo_tv_files/')

    class Meta:
        verbose_name = 'приложение NEO TV'
        verbose_name_plural = 'приложения NEO TV'

    def __str__(self):
        return self.get_type_display()
