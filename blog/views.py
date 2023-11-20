from django.shortcuts import render

from django.urls import reverse_lazy, reverse

from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

from blog.models import Blog

from pytils.translit import slugify


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'image_preview', 'is_published')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_form = form.save()
            new_form.slug = slugify(new_form.title)
            new_form.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'image_preview', 'is_published')

    def form_valid(self, form):
        if form.is_valid():
            new_form = form.save()
            new_form.slug = slugify(new_form.title)
            new_form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)

        self.object.view_count += 1
        self.object.save()

        return self.object


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)

        queryset = queryset.filter(is_published=True)

        return queryset


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')