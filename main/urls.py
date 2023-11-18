from django.urls import path

from main.views import HomeView, ContactView, CategoryProductView

from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('category_product/<int:pk>/', CategoryProductView.as_view(), name='category_product'),
]