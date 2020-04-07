from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class AuthorList(models.Model):
    author = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.author


class Post(models.Model):
    author = models.ForeignKey(AuthorList,on_delete=models.CASCADE,null=True,blank=False)
    pic = models.ImageField(upload_to="", null=True,blank=False)
    caption = models.TextField(max_length=100,blank=True,null=True)
    post_date = models.DateTimeField(default=timezone.now)
    comment = models.TextField(max_length=100,blank=True,null=True)
    def __str__(self):
         return self.caption