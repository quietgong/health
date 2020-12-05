from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import PostForm, AnswerForm
from ..models import Post, Answer

@login_required(login_url='accounts:login')
def answer_create(request, post_id):
    """
    community 답변등록
    """
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.author = request.user
            answer.post = post
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('community:detail', post_id=post.id), answer.id))
    else:
        form = AnswerForm()
    context = {'post': post, 'form': form}
    return render(request, 'community/post_detail.html', context)

@login_required(login_url='accounts:login')
def answer_modify(request, answer_id):
    """
    community 답변수정
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('community:detail', post_id=answer.post.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('community:detail', post_id=answer.post.id), answer.id))
    else:
        form = PostForm(instance=answer)
    context={'answer': answer, 'form': form}
    return render(request, 'community/answer_form.html', context)

@login_required(login_url='accounts:login')
def answer_delete(request, answer_id):
    """
    community 답변삭제
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제 권한이 없습니다.')
    else:
        answer.delete()
    return redirect('community:detail', post_id=answer.post.id)