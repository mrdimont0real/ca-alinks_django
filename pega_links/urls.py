from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrar/', views.registrar_view, name='registrar'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('members/', views.members_view, name='members'),


]
