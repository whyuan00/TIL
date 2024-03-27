from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


'''
new와 create 함수간 공통점과 차이점: get과 post
새로운 페이지 달라는 요청은 get
새로운 페이지만들때는 get이 들어오지 않음. form을통해 post가 들어옴 
메서드가 분리되어있음 
-> 하나로 합쳐서 get이면 new실행, post면 create 실행? 

'''
def create(request):
    form = ArticleForm(request.POST)
    # 포스트 먼저보는 이유는? 
    if request.method =="POST":
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail',article.pk)
    else:
        #new 함수와 동일 
        form =ArticleForm()
    # 유효성검사 실패시 여기로 옴. 인덱스 주의
    context = {
        'form':form,
    }
    return render(request,'articles/create.html',context)
'''
def new(request):
    form = ArticleForm()
    context = {
        'form':form,
    }
    return render(request, 'articles/new.html',context)


def create(request):
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # article = Article(title=title, content=content)
    # article.save()
    form = ArticleForm(request.POST) # 객체 덩어리만 넣어줌  
    #유효성 검사 후 세이브
    if form.is_valid():
        article = form.save() # save는 리턴이 있음 
        return redirect('articles:detail', article.pk)
    #유효성 검사 실패시
    context = {
        'form':form,
    }
    return render(request,'articles/new.html',context)
    # return redirect('articles:new')
    #redirect가 아닌이유? 1. form 을 못넘김 
    #2. 에러메세지x 새주소 요청 다시보내게됨
'''


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

 #업데이트와 에딧도 합칠수있음

def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method =='POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail',article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form':form,
        'article':article,
    }
    return render(request,'articles/edit.html',context)




'''

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article) # 기존인자 넣어줘야함 
    context = {
        'article': article,
        'form':form,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST,instance=article)
    # form에 인스턴스=article, 즉 기존 인자가 들어감 
    if form.is_valid():
        form.save() 
        return redirect('articles:detail', article.pk)
    context = {
        'form': form,
        'article' :article,
    }
    return render(request,'articles/edit.html',context)

    # title = request.POST.get('title')
    # content = request.POST.get('content')

    # article.title = title
    # article.content = content
    # article.save()
'''
# crud 만드는 순서
'''

def create(request):
if request.method == 'POST':
pass
else:
#아래부터 작성 
pass
'''

