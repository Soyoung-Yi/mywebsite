from django.shortcuts import render
from .models import Post, Category, Tag
from django.views.generic import ListView, DetailView


class PostList(ListView):
   model = Post

   def get_queryset(self):
      return Post.objects.order_by('title')
   def get_context_data(self, *, object_list=None, **kwargs):
      context = super(PostList, self).get_context_data(**kwargs)
      context['category'] = '모든 카테고리'
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
   context = {'post_list':post_list, 'category':category_name}
   return render(request, 'blog/post_list.html', context)

class PostListByCategory(ListView):
   def get_queryset(self):
      slug = self.kwargs['slug']
      # print(type(slug), '-',slug)
      if slug != 'None':
         category = Category.objects.get(slug=slug)
      else:
         self.kwargs['slug'] = '미분류'
         category = None
      return Post.objects.filter(category=category)

   def get_context_data(self, *, object_list=None, **kwargs):
      context = super(PostListByCategory, self).get_context_data(**kwargs)
      context['category'] = self.kwargs['slug']
      return context


class PostListByTag(ListView):
   def get_queryset(self):
      tag_name = self.kwargs['tag_name']
      print(tag_name, type(tag_name))
      try:
         tag = Tag.objects.get(name=tag_name)
      except:
         self.kwargs['tag_name'] = '태그없음'
         tag = None
      return Post.objects.filter(tags=tag)

   def get_context_data(self, *, object_list=None, **kwargs):
      context = super(PostListByTag, self).get_context_data(**kwargs)
      context['category'] = '#'+self.kwargs['tag_name']
      return context
      
