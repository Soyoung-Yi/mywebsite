from django.urls import path
from . import views
from django.views.generic import ListView
from .models import Post
app_name = 'blog'
urlpatterns = [
    # path('', views.index, name="index"),
    path('', views.PostList.as_view(), name='index'),
    # path('', ListView.as_view(model=Post)),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail'),
]