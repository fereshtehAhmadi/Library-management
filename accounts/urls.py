from django.urls import path, include
from accounts import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),
    path('logout/', views.logout_user, name='logout_user'),
]