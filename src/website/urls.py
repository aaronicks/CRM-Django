from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_user, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]
