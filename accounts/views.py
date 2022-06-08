from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.core.mail import send_mail
from library_managment import settings
from accounts.models import CustomUserModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegisterationForm, UpdateUserForm, CustomUserForm
from books.models import Categorie
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages


def user_list(request):
    content = {
        'user_list': User.objects.all(),
    }
    return render(request, 'accounts/userlist.html', content)


def delete_user(request, pk):
    obj = get_object_or_404(User, id=pk)
    obj.delete()
    return redirect('user_list')



def decline(request, pk):
    obj = get_object_or_404(User, id=pk)
    obj.is_staff=False
    obj.save()
    return redirect('user_list')    
    
    
def promote(request, pk):
    obj = get_object_or_404(User, id=pk)
    obj.is_staff=True 
    obj.save()
    return redirect('user_list')
    


@login_required(login_url='login')
def account(request):
    user_form = UpdateUserForm(request.POST, instance=request.user)
    profile = CustomUserForm(request.POST, instance=request.user)
    if request.method == 'POST':
        if profile.is_valid():
            user_form.save()
            profile = profile.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')
    content = {
        'user_form': user_form,
        'profile': profile,
        'customuser': CustomUserModel.objects.get(user=request.user),
        
    }
    return render(request, 'accounts/account.html',content)


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            messages.success(request, 'Your registration was successfully done.')
            return redirect('login_user')
        else:
            messages.error(request, 'Passwords don\'t match.')
            
    user_form = UserRegisterationForm()
    context = {
        'user_form': user_form
    }  
    return render(request,'accounts/register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username =username, password= password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password is incorrect')
    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login_user')



def about(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST['title']
        message = request.POST['message']
    
        send_mail(title, message, settings.EMAIL_HOST_USER, [user.email])
        messages.success(request, 'your massage send successfully!!')
        redirect('about')
        
    return render(request, 'other/about.html')


def advance_search(request):
    return render(request, 'other/advance_search.html')
