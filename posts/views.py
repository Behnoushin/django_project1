from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from .models import Post , Comment
from .forms import PostForm
from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET","post"])
def index (request):
    #body
    #return HttpResponse('<h1> Welcome to Django </h1>')
    #print (request.data)
    try:
        p = Post.objects.get(pk = 100)
    except Post.DoesNotExist:
        return Response ({'detail': ' Post not exits'})
    return Response ({'name':'behi'})

def home (request):
    return HttpResponse('<h3> Welcome to my blog </h3>')


def post_list(request):
    posts = Post.objects.all()
    context ={'posts' : posts}
    return render(request , 'posts/post_list.html', context = context )

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'



def post_detail(request, post_id):
    try:
        post = Post.objects.get(pk = post_id)
    except Post.DoesNotExist:
        return HttpResponseNotFound ('Post is not exist !!!')
    #post = get_object_or_404(Post,pk=post_id)
    
    comments = Comment.objects.filter(post=post)
    context ={'post' : post , 'comments':comments}
    return render(request , 'posts/post_detail.html', context = context )


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    def get_context_data(self, **kwargs):
        print(kwargs)
        context = super(PostDetail,self).get_context_data()
        context['comments'] = Comment.objects.filter(post=kwargs['object'].pk)
        return context

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print(type(form.cleaned_data))
            print(form.cleaned_data)
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/posts/')
    else:
        form = PostForm()
        
    return render(request, 'posts/post_create.html', {'form':form})