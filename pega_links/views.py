from django.shortcuts import render
from blog.models import Post, Member  
from blog.models import Member

def home(request):
    posts = Post.objects.all()
    pessoas = Member.objects.all()  
    return render(request, 'home.html', {'posts': posts, 'pessoas': pessoas})

def registrar_view(request):
    return render(request, 'registrar.html')

def members_view(request):
    pessoas = Member.objects.all()
    return render(request, 'members.html', {'pessoas': pessoas})
