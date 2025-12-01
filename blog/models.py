from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    # image
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tags
    # category
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return f"{self.title} - {self.id}"  # type: ignore