from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect

#forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from app_login.forms import SignUpForm,EditProfileForm,NewUserForm
from app_login.models import NewUser
# Create your views here.
def signup(request):
    form=SignUpForm()
    if request.method=="POST":
        form=SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    diction={'form':form}
    return render(request,'app_login/signup.html',context=diction)

def user_login(request):
    loginform=AuthenticationForm()
    if request.method=="POST":
        loginform=AuthenticationForm(data=request.POST)
        if loginform.is_valid():
            username=loginform.cleaned_data.get('username')
            password=loginform.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
    diction={"loginform":loginform}
    return render(request,'app_login/login.html',context=diction)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app_login:login'))

@login_required
def profile(request):
    diction={}
    return render(request,'app_login/profile.html',context=diction)

@login_required
def edit_profile(request):
    current_user=request.user
    form=EditProfileForm(instance=current_user)
    if request.method=="POST":
        form=EditProfileForm(request.POST,instance=current_user)
        if form.is_valid():
            form.save()
            form=EditProfileForm(instance=current_user)
            return HttpResponseRedirect(reverse('app_login:profile'))
    diction={'form':form}
    return render(request,'app_login/edit_profile.html',context=diction)

@login_required
def pro_pic_change(request):
    form=NewUserForm()
    if request.method=="POST":
        form=NewUserForm(request.POST,request.FILES)
        if form.is_valid():
            saveform=form.save(commit=False)
            saveform.user=request.user
            saveform.save()
            return HttpResponseRedirect(reverse('app_login:profile'))
    diction={"form":form}
    return render(request,'app_login/add_pro_pic.html',context=diction)

@login_required
def password_change(request):
    current_user=request.user
    form=PasswordChangeForm(current_user)
    if request.method=="POST":
        form=PasswordChangeForm(request.POST,current_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app_login:profile'))
    diction={"form":form}
    return render(request,'app_login/password_change.html',context=diction)

