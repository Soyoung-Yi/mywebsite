from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


class PostList(ListView):
   model = Post
   def get_queryset(self):
      return Post.objects.order_by('title')


def index(request):
   posts = Post.objects.all()
   return render(request, 'blog/index.html',{'posts':posts})


class PostDetail(DetailView):
   model = Post