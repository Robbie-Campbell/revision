from django.shortcuts import render
from .models import Post, Category

def home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts, "categories": categories})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    categories = Category.objects.all()
    return render(request, 'posts/post_detail.html', {'post': post, "categories": categories})

def post_categories(request, slug):
    posts = Post.objects.filter(category__slug=slug)
    categories = Category.objects.all()
    return render(request, 'posts/post_categories.html', {'posts': posts, "categories": categories})