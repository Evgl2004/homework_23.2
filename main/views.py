from django.shortcuts import render

from main.models import Product


def home(request):

    content = {
        'object_list': Product.objects.all(),
        'title': 'Главная',
        'description': 'Вся информация о товаре',
    }

    return render(request, 'main/home.html', content)


def contacts(request):

    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     phone = request.POST.get('phone')
    #     message = request.POST.get('message')
    #
    #     print(f"{name} - {phone} - {message}")

    content = {
        'title': 'Контакты',
        'description': 'Наша контактная информация',
    }

    return render(request, 'main/contacts.html', content)