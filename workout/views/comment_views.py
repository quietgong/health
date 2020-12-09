from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import CommentForm
from ..models import Answer, Comment

@login_required(login_url='accounts:login')
def comment_create(request, answer_id):
    """
    workout 답글등록
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('workout:detail', post_id=comment.answer.post.id), comment.id))
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'workout/comment_form.html', context)


@login_required(login_url='accounts:login')
def comment_modify(request, comment_id):
    """
    workout 답글수정
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('workout:detail', post_id=comment.answer.post.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('workout:detail', post_id=comment.answer.post.id), comment.id))
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'workout/comment_form.html', context)


@login_required(login_url='accounts:login')
def comment_delete(request, comment_id):
    """
    workout 답글삭제
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('workout:detail', post_id=comment.answer.post.id)
    else:
        comment.delete()
    return redirect(':detail', post_id=comment.answer.post.id)