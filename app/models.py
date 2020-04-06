from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone



class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,null=True)
    pic = models.ImageField(blank=True, null=True)
    caption = models.TextField(blank=True,null=True)
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
         return self.caption