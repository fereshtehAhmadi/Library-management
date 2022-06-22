from django.urls import path, include

from django.contrib.auth import views as auth_views
from accounts.forms import PasswordsChangeView
from accounts import views

urlpatterns = [
    path('', include('extra.urls')),
    
    path('login/', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout_user'),
    
    path('account/', views.account, name='account'),
    path('edit/', views.edit_user_info, name='edit'),
    
    path('about/', views.about, name='about'),
    
    path('new_user/', views.new_user, name='new_user'),
    path('user_list/', views.user_list, name='user_list'),
    path('user_active/<int:pk>', views.user_active, name='user_active'),
    path('user_unactive/<int:pk>', views.user_unactive, name='user_unactive'),
    path('user_detail/<int:pk>', views.user_detail, name='user_detail'),
    path('promote_user/<int:pk>', views.promote, name='promote'),
    path('decline/<int:pk>', views.decline, name='decline'),
    
    path('password/', PasswordsChangeView.as_view(template_name='accounts/change_password.html'), name='change_password'),

    path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), 
         name='reset_password'),
    
    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password-reset_sent.html'), 
         name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), 
         name='password_reset_confirm'),
    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_don.html'), 
         name='password_reset_complete'),
]