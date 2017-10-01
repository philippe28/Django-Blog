from django.shortcuts import render
from django.utils import timezone

# Create your views here.

from .models import Publicacao


def post_lista(request):
    posts = Publicacao.objects.order_by('-data_publicacao')
    return render(request, 'blog/post_lista.html', {'posts': posts})


def post(request, slug):
    post = Publicacao.objects.get(slug=slug)
    context = {
        'post': post
    }
    return render(request, 'catalog/product.html', context)
