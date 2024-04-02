from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required 

# login_required: 인증된 사용자에 대해서만view 함수 실행하는 데코레이터



# Create your views here.
def login(request):

    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context= {
        'form':form,
    }
    return render(request, 'accounts/signup.html',context)


@login_required
def delete(request):
    # request안에 user있어서 조회필요없이 삭제
    request.user.delete()
    return redirect('articles:index') 

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form,
    }

    return render(request, 'accounts/update.html',context)

@login_required
def change_password(request,user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user) # 무효화 방지 
            return redirect('articles:index')
        
        # 비번변경하면서 새로운 세션키 받음 
        # 이전 세션키로는 새로운 세션데이터 못받아서 로그인 

        # 암호변경시 세션무효화 막아주는 함수: update_session_auth_hash(requst,user)
    else:
        # passwordChangeForm 첫번째 인자는 user 
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/change_password.html',context)