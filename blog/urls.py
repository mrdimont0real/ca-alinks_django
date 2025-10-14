from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  
    path('login', views.login,name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('recuperar-senha/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('recuperar-senha/enviado/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('recuperar-senha/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('recuperar-senha/completo/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('alterar-senha/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('alterar-senha/concluido/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('registrar/', views.registrar, name='registrar'),
    path('perfil/', views.perfil_view, name='perfil'),

]


