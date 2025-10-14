from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Member(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pessoas")
    nome = models.CharField("Nome", max_length=255)
    cpf = models.CharField("CPF", max_length=15)
    email = models.EmailField("Email")
    telefone = models.CharField("Telefone", max_length=30)
    data_nascimento = models.DateField("Data de nascimento")
    rg = models.CharField("RG", max_length=30, null=True, blank=True)
    endereco = models.CharField("Endereço residencial", max_length=255, null=True, blank=True)
    bairro = models.CharField("Bairro", max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome
