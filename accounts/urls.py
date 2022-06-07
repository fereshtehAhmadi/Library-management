from django.urls import path, include

from django.contrib.auth import views as auth_views
from accounts.forms import PasswordChangeView
from accounts import views

urlpatterns = [
    path('', include('extra.urls')),
    path('login/', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),
    path('about/', views.about, name='about'),
    path('advance_search/', views.advance_search, name='advance_search'),
    path('user_list/', views.user_list, name='user_list'),
    path('delete_user/<int:pk>', views.delete_user, name='delete'),
    path('promote_user/<int:pk>', views.promote, name='promote'),
    path('decline/<int:pk>', views.decline, name='decline'),
    path('logout/', views.logout_user, name='logout_user'),
    
#     path('change_password/', 
#          auth_views.PasswordChangeView.as_view(template_name='accounts/change_password.html'), 
#          name='change_password'),
    path('change_password/', 
         PasswordChangeView.as_view(template_name='accounts/change_password.html'), 
         name='change_password'),
    
    
    
    path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), 
         name='reset_password'),
    
    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password-reset_sent.html'), 
         name='password_reset_don'),
    
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), 
         name='password_reset_confirm'),
    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_don.html'), 
         name='password_reset_complete'),
]