from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
