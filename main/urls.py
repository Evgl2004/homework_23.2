from django.urls import path

from main.views import home, contacts, category_product

from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('category_product/<int:pk>/', category_product, name='category_product'),
]