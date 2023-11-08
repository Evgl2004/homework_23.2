from django.shortcuts import render

from main.models import Product, Category


def home(request):

    content = {
        'object_list': Product.objects.all(),
        'title': 'Главная',
        'description': 'Вся информация о товаре',
    }

    return render(request, 'main/home.html', content)


def contacts(request):

    content = {
        'title': 'Контакты',
        'description': 'Наша контактная информация',
    }

    return render(request, 'main/contacts.html', content)


def category_product(request, pk):

    content = {
        'object_list': Product.objects.filter(category=pk),
        'title': 'Продукты',
        'description': f'Список продуктов {Category.objects.get(pk=pk).name}',
    }

    return render(request, 'main/category_product.html', content)