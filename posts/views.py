from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index (request):
    #body
    return HttpResponse('<h1> Welcome to Django </h1>')

def home (request):
    return HttpResponse('<h3> Welcome to my blog </h3>')

def post_list(request):
    posts = Post.objects.all()
    context ={'posts' : posts}
    return render(request , 'posts/post_list.html', context = context )

def post_detail(request , post_id):
    posts = Post.objects.get(pk = post_id)
    context ={'posts' : posts}
    return render(request , 'post_detail.html', context = context )