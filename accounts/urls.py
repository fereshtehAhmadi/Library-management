from django.urls import path, include
from accounts import views

urlpatterns = [
    path('', include('extra.urls')),
    path('login/', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),
    path('change_password/', views.change_password, name='change_password'),
    path('about/', views.about, name='about'),
    path('advance_search/', views.advance_search, name='advance_search'),
    path('user_list/', views.user_list, name='user_list'),
    path('delete_user/<int:pk>', views.delete_user, name='delete'),
    path('promote_user/<int:pk>', views.promote, name='promote'),
    path('decline/<int:pk>', views.decline, name='decline'),
    path('logout/', views.logout_user, name='logout_user'),
]