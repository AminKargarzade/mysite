from django import template
from blog.models import Post

register = template.Library()

@register.simple_tag(name='totalposts')
def function():
    return Post.objects.filter(status=1).count()

@register.simple_tag(name='posts')
def function2():
    return Post.objects.filter(status=1)

@register.filter(name='snippet')
def snippet(value,arg=20):  # sourcery skip: use-fstring-for-concatenation
    return value[:arg] + '...' if len(value) > 100 else value

@register.inclusion_tag('popular_posts.html')
def popular_posts():
    posts = Post.objects.filter(status=1).order_by('published_date')[:4]
    return {'posts': posts}