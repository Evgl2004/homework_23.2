from django.conf import settings
from django.core.cache import cache

from main.models import Category


def get_cached_category_list():

    if settings.CACHE_ENABLED:
        category_list = cache.get('category_list')

        if category_list is None:
            category_list = Category.objects.all()
            cache.set('category_list', category_list)
    else:
        category_list = Category.objects.all()

    return category_list
