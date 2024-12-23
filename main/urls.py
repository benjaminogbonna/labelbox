from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
]