from django.shortcuts import render
from django.utils import timezone

# Create your views here.

from .models import Publicacao, Contato
from .forms import ContatoForm


def post_lista(request):

    posts = Publicacao.objects.order_by('-data_publicacao')

    form = ContatoForm(request.POST or None)
    if form.is_valid():
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        post = form.save(commit=False)
        post.nome = request.POST['nome']
        post.email = request.POST['email']
        post.ip = ip

        post.save()

    return render(request, 'blog/post_lista.html', {'posts': posts})


def post(request, slug):
    post = Publicacao.objects.get(slug=slug)
    print(slug)

    return render(request, 'blog/post_detalhe.html', {'post': post})


def contato(request):
    success = False
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.nome = request.nome
        post.email = request.email
        print(post.nome)
        post.save()

    return render(request, 'contato.html', context)
