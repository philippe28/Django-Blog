from django.shortcuts import render
from django.utils import timezone

# Create your views here.

from .models import Publicacao
from .forms import Contato


def post_lista(request):
    
    posts = Publicacao.objects.order_by('-data_publicacao')
    return render(request, 'blog/post_lista.html', {'posts': posts})


def post(request, slug):
    post = Publicacao.objects.get(slug=slug)

    print(slug)

    return render(request, 'blog/post_detalhe.html', {'post': post})

def contato(request):
    success = False
    form = Contato(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido')
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contato.html', context)
