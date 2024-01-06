from django.shortcuts import render

from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView, TemplateView

from main.models import Product, Category, Version

from main.forms import ProductFromUser, ProductFromModerator, VersionForm

from django.urls import reverse_lazy, reverse

from django.forms import inlineformset_factory

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

from django.shortcuts import redirect, Http404


class HomeView(ListView):
    model = Product
    extra_context = {
        'title': 'Главная',
        'description': 'Вся информация о товаре',
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)

        for product in queryset:
            version = product.version_set.all().filter(is_current=True).first()
            product.version = version

        return queryset


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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductFromUser
    success_url = reverse_lazy('main:home')

    extra_context = {
        'title': 'Добавить продукт',
        'description': 'Новый продукт',
    }

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductFromUser

    def get_success_url(self):
        return reverse('main:edit_product', args=[self.kwargs.get('pk')])

    extra_context = {
        'title': 'Изменить продукт',
        'description': 'Редактировать продукт',
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']

        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_form_class(self):
        if is_moderator(self.request.user):
            return ProductFromModerator
        else:
            return ProductFromUser

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner == self.request.user or is_moderator(self.request.user) or self.request.user.is_superuser:
            return self.object
        else:
            raise Http404("Доступ только для владельца")


def is_moderator(user):
    return user.groups.filter(name='moderator').exists()


class ProductDetailView(DetailView):
    model = Product

    extra_context = {
        'title': 'Просмотр продукта',
        'description': 'Информация о продукте',
    }


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('main:home')

    permission_required = 'main.delete_product'

    extra_context = {
        'title': 'Удалить продукт',
        'description': 'Подтверждение удаление продукта',
    }

