from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return '{}::{}'.format(self.name, self.description)


class Post(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True,
                                 on_delete=models.SET_NULL)
    title = models.CharField(max_length=30)
    content = models.TextField()
    head_image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True)
    created = models.DateTimeField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}::{}-{}".format(self.title, self.author,self.created)

    def get_absolute_url(self):
        return '/blog/{}/'.format(self.pk)
        # return reverse('blog:detail', args=[self.id])

    class Meta:
        ordering = ['-created']