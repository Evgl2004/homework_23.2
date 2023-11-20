from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'image_preview', 'is_published')
    success_url = reverse_lazy('blog:list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'image_preview', 'is_published')
    success_url = reverse_lazy('blog:list')


class BlogDetailView(DetailView):
    model = Blog


class BlogListView(ListView):
    model = Blog


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')