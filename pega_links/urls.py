from django.contrib import admin
from django.urls import path, include
from blog import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # ou 'blog/' se quiser prefixar
    path('login/', views.login_view, name='login'),
    path('alterar-senha/', auth_views.PasswordChangeView.as_view(), name='alterar_senha'),
    path('', include('pega_links.urls')),
]