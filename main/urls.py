from django.urls import path

from main.views import (HomeView, ContactView, CategoryProductView, ProductCreateView, ProductDetailView,
                        ProductUpdateView, ProductDeleteView)

from main.apps import MainConfig

from django.views.decorators.cache import cache_page

app_name = MainConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('category_product/<int:pk>/', CategoryProductView.as_view(), name='category_product'),
    path('product/create/', ProductCreateView.as_view(), name='create_product'),
    path('product/edit/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
    path('product/view/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='view_product'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
]