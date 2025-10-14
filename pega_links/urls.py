from django.contrib import admin
from django.urls import path, include
from ..blog import views

urlpatterns = [
     path('', include('blog.urls')), 
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')), 
    path('login/', views.login_view, name='login'),

]