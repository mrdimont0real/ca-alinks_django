from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from blog.models import Member, Post

def home(request):
    posts = Post.objects.all()
    pessoas = Member.objects.all()
    return render(request, 'home.html', {'posts': posts, 'pessoas': pessoas})

def testing(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('perfil')  # redireciona para a tela de perfil
        else:
            erro = "Usuário ou senha inválidos"
            return render(request, 'login.html', {'erro': erro})
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # redireciona para login após logout

def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registrar.html', {'form': form})

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

@login_required
def perfil_view(request):
    return render(request, 'perfil.html', {'user': request.user})
