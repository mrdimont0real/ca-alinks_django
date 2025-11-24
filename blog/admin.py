from django.contrib import admin
from .models import Post, Pessoa


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_criacao')   
    search_fields = ('titulo', 'conteudo')
    list_filter = ('data_criacao',)


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'idade')
    search_fields = ('nome', 'email')
    list_filter = ('idade',)
    fieldsets = (
        ('Informações Pessoais', {'fields': ('nome', 'rg')}),
        ('Contato', {'fields': ('telefone',)}),
    )
