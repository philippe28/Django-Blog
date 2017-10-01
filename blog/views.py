from django.shortcuts import render
from django.utils import timezone

# Create your views here.

from .models import Publicacao


def post_lista(request):
    posts = Publicacao.objects.filter(
        data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    return render(request, 'blog/post_lista.html', {'posts': posts})
