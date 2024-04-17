from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article,Comment

from django.shortcuts import get_object_or_404,get_list_or_404
# getobject : get 없으면 404 반환 
# getlist: filter 없으면 404 반환
@api_view(['GET'])
def comment_list(request):
    # 전ㅊ 댓글 조회
    # comments = Comment.objects.all()
    comments = get_list_or_404(Comment)
    # 직렬화
    serializer = CommentSerializer(comments,many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request,comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method =='GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    
    elif request.method =='PUT':
        serializer=CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save() # 이미 comment정보 남아있어서 저장만하면됨
            return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(
            article, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def comment_create(request,article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    # 입력 데이타 받아서 작업 진행 
    serializer = CommentSerializer(data=request.data)
    # 커멘트시리얼라이저는 아티클에 대한 것도 같이 검사 진행 
    # 유효성 검사에서는 제외하고 데이터 조회사에는 출력하는 필드로 옵션 바꿔주기

    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article) # commit false 없어서 save에 외래키넣어줌
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    