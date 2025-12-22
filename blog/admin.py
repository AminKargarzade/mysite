from django.contrib import admin
from blog.models import Post,Category,Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'counted_views', 'status', 'login_required', 'published_date', 'created_date')
    list_filter = ('status', 'author', 'published_date', 'created_date')
    # ordering = ('-created_date',)
    search_fields = ('title', 'content')
    summernote_fields = ('content',)
    
admin.site.register(Category)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'post', 'approved', 'created_date')
    list_filter = ('post', 'approved')
    search_fields = ['name', 'post']