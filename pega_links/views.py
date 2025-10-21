from blog.models import Post, Member  # certifique-se de que Member é o modelo correto

def home(request):
    posts = Post.objects.all()
    pessoas = Member.objects.all()  # ou Pessoa.objects.all() se o nome for diferente
    return render(request, 'home.html', {'posts': posts, 'pessoas': pessoas})
