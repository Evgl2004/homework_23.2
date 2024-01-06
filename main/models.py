from django.db import models
from datetime import datetime

from django.conf import settings

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')

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

    is_published = models.BooleanField(default=True, verbose_name='опубликовано')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return f'{self.name} {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

        permissions = [
            (
                'set_published',
                'Возможно опубликовать продукт'
            )
        ]


class Contacts(models.Model):
    country = models.CharField(max_length=50, verbose_name='страна')
    inn = models.CharField(max_length=15, verbose_name='страна')
    address = models.CharField(max_length=100, verbose_name='адрес')

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'

    def __str__(self):
        return f'{self.inn}'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number = models.CharField(max_length=15, verbose_name='номер')
    name = models.CharField(max_length=100, verbose_name='название')
    is_current = models.BooleanField(verbose_name='текущий')

    def __str__(self):
        return f'{self.number} - {self.name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

