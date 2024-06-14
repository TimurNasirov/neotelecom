from django.db import models


class ProductionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_visible=True, is_delete=False)
