from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

# from django.views.decorators.http import require_http_methods

from django.contrib.auth import get_user_model  
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("boards:index")
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)




def logout(request):
    auth_logout(request)
    return redirect('boards:index')


def profile(request,person_pk):
    person = get_user_model().objects.get(pk=person_pk)
    boards = person.board_set.all() 
    comments = person.comment_set.all()
    followers = person.followers.all()
    context = {
        'person':person,
        'boards':boards,
        'comments':comments,
        'followers':followers,
    }
    return render(request, 'accounts/profile.html',context)        

@login_required
def follow(request,person_pk):
    # 팔로우 데이터 저장/삭제 
    # post만 벋울곳 
    user = request.user 
    person = get_user_model().objects.get(pk=person_pk)
    # 버튼 누른 사람의 pk가 이미 follower 리스트에 있는경우딜리트
    if user !=person:
        if user in person.followers.all():
            person.followers.remove(user)
        # 없는경우 에드
        else:
            person.followers.add(user) 
        
        return redirect('accounts:profile',person_pk)