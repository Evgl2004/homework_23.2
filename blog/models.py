from django.db import models
from datetime import datetime

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=250, verbose_name='slug')
    content = models.TextField(**NULLABLE, verbose_name='содержимое')
    image_preview = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='изображение (превью)')
    data_create = models.DateTimeField(default=datetime.now(), verbose_name='дата создания')
    is_published = models.BooleanField(default=False, verbose_name='опубликовано')
    view_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'

