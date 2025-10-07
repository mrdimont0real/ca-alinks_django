

from .models import Post


from django.contrib import admin  
# Register your models here.

admin.site.register(Post)
from django.contrib import admin
from .models import Post  # ← essa linha importa o modelo Post

