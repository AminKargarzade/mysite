from unicodedata import category
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager # type: ignore

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = TaggableManager(blank=True)
    category = models.ManyToManyField('Category',blank=True)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    login_required = models.BooleanField(default=False)
    published_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return f"{self.title} - {self.id}"  # type: ignore
    
    # def snippet(self):
    #     return self.content[:100] + "..."
    
    def get_absolute_url(self):
        return reverse('blog:single',kwargs={'pid':self.id}) # type: ignore
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"