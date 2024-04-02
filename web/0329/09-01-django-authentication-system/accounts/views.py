from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login# 세션데이터 생성해서 로그인 데이터만드는함수
from django.contrib.auth import logout as auth_logout
# db의 세션데이터& 쿠키에서 세션id 없애서 로그아웃하는 함수
# Create your views here.

def login(request):
    if request.method =="POST":
        #모델폼이아님 -> 생성자 함수 구성도 다름
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())# isvalid 통과한 user객체.form에서 user만 
            #form.save()--> 저장 아니고 로그인 시켜야함 
            return redirect('articles:index')
        
        # 로그인중인지 확인: db에서 세션 생성되어있는지/ 크롬에서 세션id부여되어있는지

    else:
        # 로그인 페이지 get요청일때:
        form = AuthenticationForm()
        # 인증관련데이ㅌ는 이미 context에 들어가있음 
        #(세팅의 템플릿-> auth에서 확인가능)
    context = {
            'form' : form, 
    }
    return render(request, 'accounts/login.html',context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')
 