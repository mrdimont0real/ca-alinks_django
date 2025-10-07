from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member
from .models import Post
from django.shortcuts import render


def home(request):
    return HttpResponse("<h1>Bem-vindo ao Blog!</h1>")


def home(request):
    return render(request, 'home.html')




def testing(request):
  posts = Post.objects.all().values()
  template = loader.get_template('home.html')
  context = {
    'posts': posts,
  }
  return HttpResponse(template.render(context, request))



def login(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        senha = request.POST.get("senha")
        posts = Post.objects.all().values()
        print(nome)
        print(senha)
        return render(request, 'home.html', locals())

    return render(request, 'login.html', locals())

from django.contrib.auth import logout
from django.shortcuts import render

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')