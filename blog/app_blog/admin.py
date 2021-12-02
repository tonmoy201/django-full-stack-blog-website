from django.contrib import admin
from django.contrib.auth.models import User 
from app_blog.models import Blog,Comment,Like
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display=['author_name','blog_title','published_date','update_date',]
    search_fields=['author_name','blog_title','published_date','update_date',]
admin.site.register(Blog,BlogAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display=['blog','user','comment','comment_date',]
    search_fields=['blog','user','comment','comment_date',]

admin.site.register(Comment,CommentAdmin)

class LikeAdmin(admin.ModelAdmin):
    list_display=['blog','user']
    search_fields=['blog','user']
admin.site.register(Like,LikeAdmin)
