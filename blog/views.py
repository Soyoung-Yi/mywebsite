from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView, DetailView


class PostList(ListView):
   model = Post

   def get_queryset(self):
      return Post.objects.order_by('title')
   def get_context_data(self, *, object_list=None, **kwargs):
      context = super(PostList, self).get_context_data(**kwargs)
      context['category_list'] = Category.objects.all()
      context['post_without_category'] = Post.objects.filter(category=None).count()
      return context

def index(request):
   posts = Post.objects.all()
   return render(request, 'blog/index.html',{'posts':posts})


class PostDetail(DetailView):
   model = Post


def searchList(request, category_name):
   try :
      category = Category.objects.get(name=category_name)
   except:
      category = None
   post_list = Post.objects.filter(category=category)
   context = {'post_list':post_list}
   return render(request, 'blog/post_list.html', context)