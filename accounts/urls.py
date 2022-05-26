from django.urls import path, include
from accounts import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),
    path('change_password/', views.change_password, name='change_password'),
    path('about/', views.about, name='about'),
    path('logout/', views.logout_user, name='logout_user'),
]