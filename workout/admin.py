from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    search_fields = ['subject']
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['subject']
admin.site.register(Comment, CommentAdmin)
