from django.shortcuts import render,redirect
from .models import Article 
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request,'articles/index.html',context)

def detail(request, pk): #url에서 pk로 변수줘서 같이받음
    article = Article.objects.get(pk=pk) 
    context = {
        # html에 보일때 쓸 변수 이름: 위에서 지정한 내용변수 
        'article': article,
    } 
    return render(request,'articles/detail.html',context)

def new(request):
    return render(request,'articles/new.html')

def create(request):
    
    # print(request.GET) 
    # <QueryDict: {'title': ['제목'], 'content': ['내용']}>
    # GET은 조회지만 POST는 디비에 추가요구: 보안이필요함
    # POST의 포비든에러 메세지 403: 권한 없음
    # POST는 CSRF 토큰 요구 -> 장고가 만든 페이지가 맞는지 확인필요 
    title = request.POST.get('title')
    content =  request.POST.get('content')

    # 첫번째
    # article = Article()
    # article.title = title
    # article.content = content 
    # article.save()

    #두번쨰 -> 짧음 & 유효성 검증 때문에 이거 쓸것 
    article = Article(title=title, content=content)
    article.save()

    #세번쨰
    # article = Article.objects.create(title=title, content=content)
    
    # return render(request,'articles/create.html') 아닌,
    # post 후에 redirect 할것: 클라이언트가 새로운 url로요청
    # 단 파이썬이라 url 디테일 <int:pk>은 못씀 ->
    # save가 끝나면 article 에 pk가 부여되기때문에 pk로 이동 
    return redirect('articles:detail',article.pk)

def delete(request,pk):
    # 몇번 글 삭제할건지 조회 먼저
    article = Article.objects.get(pk=pk) 
    article.delete() 
    return redirect('articles:index')

def edit(request,pk):
    article = Article.objects.get(pk=pk) 
    context = {

        'article': article 
    }
    return render(request,'articles/edit.html',context)

def update(request,pk):
    # update는 create 와 아주 유사함 
    # n번게시글 수정 -> 조회 필요 
    article = Article.objects.get(pk=pk) 
    title = request.POST.get('title')
    content =  request.POST.get('content')

    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail',article.pk)