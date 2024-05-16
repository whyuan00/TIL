from django.shortcuts import render
from .models import Article, Comment
from django.db.models import Count


# Create your views here.
def index_1(request):
    # articles = Article.objects.order_by('-pk')
    # articles 라는 필드에 댓글개수 센 필드를 넣겠다 :  annotate 주석을 붙여주겠다
    articles = Article.objects.annotate(Count('comment')).order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_1.html', context)


def index_2(request):
    # articles = Article.objects.order_by('-pk')
    # article 가져올때 각 article 에 포함된 user(참조관계)도 가져옴 
    articles = Article.objects.select_related('user').order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_2.html', context)


def index_3(request):
    # articles = Article.objects.order_by('-pk')
    #다대다 또는 역참조관계 일때 최적화 -> 게시글조회하면서 댓글모음 가져오기(1:N 역참조)
    articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_3.html', context)


from django.db.models import Prefetch


def index_4(request):
    # articles = Article.objects.order_by('-pk')
    # 댓글 목록 가져올때는 최적화가 많이 안됨
    # articles = Article.objects.prefetch_related('comment_set').order_by('-pk')

    # 댓글목록 가져오면서 user까지 같이 가져오는게 좋음, 게시글->댓글과 user 는 역참조
    articles = Article.objects.prefetch_related(
        # 댓글목록과 각 댓글에 따른 user 한방에 가져옴 
        Prefetch('comment_set', queryset=Comment.objects.select_related('user'))
    ).order_by('-pk')

    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_4.html', context)
