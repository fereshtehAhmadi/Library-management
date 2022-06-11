from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.core.mail import send_mail
from library_managment import settings

from django.contrib.auth.models import User
from accounts.models import CustomUserModel
from books.models import Categorie

from accounts.forms import UserRegisterationForm

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def user_list(request):
    content = {
        'user_list': User.objects.order_by('username'),
    }
    return render(request, 'accounts/userlist.html', content)


def user_detail(request,pk):
    user = User.objects.get(id=pk)
    validation = CustomUserModel.objects.filter(user=user).exists()
    if validation:
        custom_user = CustomUserModel.objects.get(user=user)
    else:
        custom_user = None
    return render(request, 'accounts/user_detail.html', {'user':user, 'custom_user': custom_user})


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
    validation = CustomUserModel.objects.filter(user= request.user).exists()
    user = User.objects.get(username=request.user.username)
    if not validation:
        if request.method == 'POST':
            user.username = request.POST['username']
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
            
            phone= request.POST['phone']
            address = request.POST['address']
            national_code = request.POST['national_code']
            age = request.POST['age']
            gender = request.POST['gender']
            customuser = CustomUserModel(
                user=user, phone=phone,
                address=address, national_code=national_code,
                age=age, gender=gender,
            )
            customuser.save()
            return redirect('home')
        return render(request, 'accounts/custom_user.html', {'user':user})
    else:
        custom_user_obj = CustomUserModel.objects.get(user=request.user)
        content = {
            'custom_user': custom_user_obj,
        }
        return render(request, 'accounts/account.html', content)
    
    
    
@login_required(login_url='login')
def edit_user_info(request):
    custom_user = CustomUserModel.objects.get(user=request.user)
    user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        
        user.username = username
        user.email = email
        user.save()
        custom_user.phone = phone
        custom_user.address = address
        custom_user.save()
        return redirect('account')
    content = {
        'custom_user': custom_user,
    }
    return render(request, 'accounts/edit_user_info.html', content)
        


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
