from django.contrib import admin
from .models import Post, Answer, Comment

class PostAdmin(admin.ModelAdmin):
    search_fields = ['subject']
admin.site.register(Post, PostAdmin)

class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['subject']
admin.site.register(Answer, AnswerAdmin)

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['subject']
admin.site.register(Comment, CommentAdmin)
