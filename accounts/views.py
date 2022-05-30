from django.shortcuts import render, redirect
from accounts.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegisterationForm, UpdateUserForm, ProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'accounts/change_password.html', {'form': form})


@login_required(login_url='login')
def account(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile = ProfileForm(request.POST, instance=request.user)
        if user_form.is_valid() and profile.is_valid():
            edit_user = user_form.save(commit=False)
            edit_user.set_password(user_form.cleaned_data['password'])
            edit_user.save()
            obj = Profile.objects.get(user= edit_user)
            n = Profile(profile, user= obj)
            n.save()
    user_form = UpdateUserForm(request.POST, instance=request.user)
    profile = ProfileForm(request.POST, instance=request.user)
    return render(request, 'accounts/account.html', {'edit': user_form, 'profile': profile})


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
    return render(request, 'accounts/about.html')


def advance_search(request):
    return render(request, 'other/advance_search.html')
