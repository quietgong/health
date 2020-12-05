from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from ..models import Post

#@login_required(login_url='accounts:login')
def list(request):
    """
    community 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    so = request.GET.get('so', 'recent') # 정렬기준

    # 정렬
    if so == 'recommend':
        post_list = Post.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        post_list = Post.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    elif so == 'history':
        post_list = Post.objects.order_by('create_date')
    else:  # recent
        post_list = Post.objects.order_by('-create_date')

    # 검색
    if kw:
        post_list = post_list.filter(
            Q(subject__icontains=kw) | # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw) # 답변 글쓴이검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(post_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'post_list': page_obj, 'page': page, 'kw': kw, 'so': so} # page, kw, so가 추가되었다.

    return render(request, 'community/post_list.html', context)

def detail(request, post_id):
    """
    community 내용 출력
    """
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'community/post_detail.html', context)