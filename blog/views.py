from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from blog.models import Member, Post



def home(request):
    return render(request, 'home.html')


def testing(request):
    posts = Post.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) 
            return redirect('home')
        else:
            erro = "Usuário ou senha inválidos"
            return render(request, 'login.html', {'erro': erro})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registrar.html', {'form': form})


@login_required
def alterar_senha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  
            return render(request, 'senha_alterada.html')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'alterar_senha.html', {'form': form})
