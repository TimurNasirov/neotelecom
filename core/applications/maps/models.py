from django.db import models


class Map(models.Model):
    MAP_TYPE_CHOICES = (
        ('4g', '4G'),
        ('gpon', 'GPON'),
        ('smart_tv', 'Smart TV'),
    )

    map_type = models.CharField('Тип карты', max_length=20, choices=MAP_TYPE_CHOICES)
    name = models.CharField('Название зоны', max_length=100)
    coordinates = models.TextField('Координаты краёв зоны',
                                   help_text='Вводятся координаты в формате *долгота,широта долгота,широта* и т.д.')

    class Meta:
        ordering = ['map_type']
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'

    def __str__(self):
        return self.get_map_type_display()

    def get_coordinates(self):
        coordinates = []
        for dot in self.coordinates.split():
            cor = [float(cor_dot) for cor_dot in dot.split(',')]
            cor.reverse()
            coordinates.append(cor)
        return coordinates
