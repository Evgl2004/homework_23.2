from django.urls import path

from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('list/', BlogListView.as_view(), name='list'),
    path('detail/<int:pk>', BlogDetailView.as_view(), name='detail'),
    path('edit/<int:pk>', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),
]