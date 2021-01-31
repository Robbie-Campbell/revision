from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post, Category

class HomeView(TemplateView):
    template_name = 'posts/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'posts/post_detail.html', {'post': post})

def post_categories(request, slug):
    posts = Post.objects.filter(category__slug=slug)
    return render(request, 'posts/post_categories.html', {'posts': posts})