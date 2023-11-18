from django.shortcuts import render

from django.views.generic import ListView, TemplateView

from main.models import Product, Category


class HomeView(ListView):
    model = Product
    extra_context = {
        'title': 'Главная',
        'description': 'Вся информация о товаре',
    }


class ContactView(TemplateView):
    template_name = 'main/contacts.html'
    extra_context = {
        'title': 'Контакты',
        'description': 'Наша контактная информация',
    }


class CategoryProductView(TemplateView):
    template_name = 'main/category_product.html'
    extra_context = {
        'title': 'Продукты',
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data['object_list'] = Product.objects.filter(category=self.kwargs.get('pk'))
        context_data['description'] = f"Список продуктов {Category.objects.get(pk=self.kwargs.get('pk')).name}",

        return context_data

