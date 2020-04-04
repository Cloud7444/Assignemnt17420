from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone



class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    pic = models.ImageField(blank=True, null=True)
    caption = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.caption