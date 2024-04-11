
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ArticleListSerializer

from rest_framework import  status

from .models import Article
#drf view에 데코레이터 필수, 다른 method는 now allowed
@api_view(['GET','POST'])
def article_list(request):
    if request.method =='GET':
        articles = Article.objects.all()
        # 변환(serialization)
        serializer = ArticleListSerializer(articles, many=True) # 다중데이터(쿼리셋)라 many
        return Response(serializer.data)# .data로 꺼내주기, 페이지없이 응답
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        #drf도 유효성검사,저장 문법 동일 
        if serializer.is_valid():
            serializer.save()
        
        # 데이터 생성 성공/실패시 응답 분리
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from .serializers import ArticleSerializer 

# delete 삭제할떄도 조회&삭제할pk 필요
# put 수정할떄도 조회,pk필요 
@api_view(['GET','DELETE','PUT'])
def article_detail(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method =='DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method =='PUT':
        # 시리얼라이저 이거인 이유: 생성일수정일중 수정일이 변화일어남
        # list는 걔네 유효성검사가 안일어남(필드)
        # partial:  부분만 수정할때 부분 데이터를 보내줌,필수는아님 
        serializer = ArticleSerializer(article,data=request.data, partial=True)
        if serializer.is_valid():
            # serializer.is_valid(raise_exception=True): 이거하면 자동으로 badrequest 반환, 제일밑return불필요
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)