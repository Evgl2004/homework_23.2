from django.db import models
from datetime import datetime


NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    created_at = models.DateTimeField(default=datetime.now, verbose_name='дата создания')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):

    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    image_preview = models.ImageField(upload_to='product/', **NULLABLE, verbose_name='изображение (превью)')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.FloatField(verbose_name='цена за покупку')
    date_creation = models.DateTimeField(default=datetime.now, verbose_name='дата создания')
    date_modification = models.DateTimeField(default=datetime.now, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
