from django.contrib import admin
from django.urls import path, include
from blog import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('blog.urls')), 
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')), 
    path('login/', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('alterar-senha/', views.alterar_senha_view, name='alterar_senha'),
    path('alterar-senha/', auth_views.PasswordChangeView.as_view(), name='alterar_senha'),
    path('', include('pega_links.urls')),
    path('alterar-senha/', views.alterar_senha, name='alterar_senha'),
    


]