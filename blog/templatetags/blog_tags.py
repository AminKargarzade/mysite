from django import template
from blog.models import Post

register = template.Library()

@register.simple_tag(name='totalposts')
def function():
    return Post.objects.filter(status=1).count()

@register.simple_tag(name='posts')
def function2():
    return Post.objects.filter(status=1)