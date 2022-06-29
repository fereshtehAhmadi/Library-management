from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.core.mail import send_mail
from library_managment import settings

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from accounts.decorators import unauthenticated_user, super_user, staff_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.http import HttpResponse
from .decorators import unauthenticated_user, super_user, staff_user

from accounts.forms import CustomUserForm, UserRegisterationForm, EditCustomUser
from accounts.models import CustomUserModel
from books.models import Categorie


@login_required(login_url='login')
@staff_user 
def user_active(request, pk):
    try:
        user = CustomUserModel.objects.get(user_id=pk)
        user.condition = True
        user.save()
    except:
        messages.error(request, 'The user must complete their information!!!')
        
    return redirect('user_detail', pk=pk)


@login_required(login_url='login')
@staff_user 
def user_unactive(request, pk):
    user = CustomUserModel.objects.get(user_id=pk)
    user.condition = False
    user.save()
    return redirect('user_detail', pk=pk)


@login_required(login_url='login')
@staff_user 
def new_user(request):
    content = {
        'user':CustomUserModel.objects.filter(condition=False),
    }
    return render(request, 'accounts/new_users.html', content)



@login_required(login_url='login')
@staff_user
def user_list(request):
    content = {
        'user_list': User.objects.order_by('username'),
        
    }
    return render(request, 'accounts/userlist.html', content)


@login_required(login_url='login')
@staff_user
def user_detail(request,pk):
    user_info = User.objects.get(id=pk)
    validation = CustomUserModel.objects.filter(user=user_info).exists()
    if validation:
        custom_user = CustomUserModel.objects.get(user=user_info)
    else:
        custom_user = None
    return render(request, 'accounts/user_detail.html', {'user_info':user_info, 'custom_user': custom_user})


@login_required(login_url='login')
@super_user
def decline(request, pk):
    obj = get_object_or_404(User, id=pk)
    obj.is_staff=False
    obj.save()
    return redirect('user_list')    
    
 
@login_required(login_url='login')
@super_user  
def promote(request, pk):
    obj = get_object_or_404(User, id=pk)
    obj.is_staff=True 
    obj.save()
    return redirect('user_list')
    

@login_required(login_url='login')
def account(request):
    validation = CustomUserModel.objects.filter(user= request.user).exists()
    user = User.objects.get(username=request.user.username)
    custom_user_form = CustomUserForm(request.POST)
    if not validation:
        if request.method == 'POST':
            if custom_user_form.is_valid():
                user.username = request.POST['username']
                user.first_name = request.POST['first_name']
                user.last_name = request.POST['last_name']
                user.email = request.POST['email']
                user.save()
                cd = custom_user_form.cleaned_data
                phone= cd['phone']
                address = cd['address']
                national_code = cd['national_code']
                birthday = cd['birthday']
                gender = cd['gender']
                customuser = CustomUserModel.objects.create(
                    user=user, phone=phone,
                    address=address, national_code=national_code,
                    birthday=birthday, gender=gender,
                )
                return redirect('home')
            else:
                messages.error(request, custom_user_form.errors)
        return render(request, 'accounts/custom_user.html', {'user':user, 'profile':custom_user_form})
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
    custom_user_form = EditCustomUser(request.POST)

    if request.method == 'POST':
        try:
            user.username = request.POST['username']
            user.email = request.POST['email']
            user.save()
        except:
            messages.error(request, 'this username already exists!!')
            return redirect('edit')
        if custom_user_form.is_valid():
            cd = custom_user_form.cleaned_data
            phone= cd['phone']
            address = request.POST['address']
            custom_user.phone = phone
            custom_user.address = address
            custom_user.save()
        else:
            messages.error(request, custom_user_form.errors)
            return redirect('edit')
        
                
        return redirect('account')
    content = {
        'custom_user': custom_user,
        'custom_user_form': custom_user_form,
    }
    return render(request, 'accounts/edit_user_info.html', content)
        

@unauthenticated_user
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


@unauthenticated_user
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
    try:
        if request.method == 'POST':
            user = request.user
            title = request.POST['title']
            message = request.POST['message']
        
            send_mail(title, message, settings.EMAIL_HOST_USER, [user.email])
            messages.success(request, 'your massage send successfully!!')
            redirect('about')
    except:
        message.erorr(request, 'Please complete your information first !!!')
    return render(request, 'other/about.html')

