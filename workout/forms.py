from django import forms
from workout.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subject', 'content', 'video_url', 'upload_files',]
        labels = {
            'subject': '제목',
            'content': '내용',
            'video_url': '동영상 주소',
            'upload_files': '썸네일',
        }
        # widget 항목 삭제 (목적 : 디자인 영역과 서버 영역 분리)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }