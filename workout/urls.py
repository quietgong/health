from django.urls import path

from .views import base_views, post_views, comment_views, vote_views

app_name = 'workout'

urlpatterns = [

    path('<int:post_id>/', base_views.detail, name='detail'),
    # post_views.py
    path('post/list/', base_views.list, name='list'),
    path('post/create/', post_views.post_create, name='post_create'),
    path('post/modify/<int:post_id>/', post_views.post_modify, name='post_modify'),
    path('post/delete/<int:post_id>/', post_views.post_delete, name='post_delete'),

    # comment_views.py
    path('comment/create/answer/<int:answer_id>/', comment_views.comment_create, name='comment_create'),
    path('comment/modify/answer/<int:comment_id>/', comment_views.comment_modify, name='comment_modify'),
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_delete, name='comment_delete'),

    # vote_views.py
    path('vote/post/<int:post_id>/', vote_views.vote_post, name='vote_post'),

# 파일업로드 추가
    path('download/<int:pk>', post_views.post_download_view, name="post_download"),
]