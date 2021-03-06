import datetime
from django.shortcuts import render
from django.utils import timezone
from django.template import loader, Context
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
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
        post.nome = request.POST['nome'] +" "+request.POST['sobrenome']
        post.email = request.POST['email']
        post.ip = ip
        post.save()

    return render(request, 'blog/post_lista.html', {'posts': posts})


def post(request, slug):
    post = Publicacao.objects.get(slug=slug)
    print(slug)

    return render(request, 'blog/post_detalhe.html', {'post': post})


def contato(request):

    form = ContatoForm(request.POST or None)
    if form.is_valid():
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        contato = form.save(commit=False)
        contato.nome = request.POST['nome'] +" "+request.POST['sobrenome']
        contato.email = request.POST['email']
        contato.ip = ip
        contato.save()

    return render(request, 'blog/contato.html',)

def tabela(request):
    tabela = Contato.objects.order_by('nome')
	
    return render(request, 'blog/tabela.html',{'tabela': tabela})

def landing(request):

    form = ContatoForm(request.POST or None)
    if form.is_valid():
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        contato = form.save(commit=False)
        contato.nome = request.POST['nome'] +" "+request.POST['sobrenome']
        contato.email = request.POST['email']
        contato.ip = ip
        contato.save()

    return render(request, 'blog/landing.html',)
	
def softskills(request):

    form = ContatoForm(request.POST or None)
    if form.is_valid():
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        contato = form.save(commit=False)
        contato.nome = request.POST['nome'] +" "+request.POST['sobrenome']
        contato.email = request.POST['email']
        contato.ip = ip
        contato.save()

    return render(request, 'blog/softskills.html',)
	
def metricaspararh(request): 

    form = ContatoForm(request.POST or None)
    if form.is_valid():
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        contato = form.save(commit=False)
        contato.nome = request.POST['nome'] +" "+request.POST['sobrenome']
        contato.email = request.POST['email']
        contato.ip = ip
        contato.save() 

    return render(request, 'blog/metricaspararh.html',)
	

def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@alo.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('blog/contato.html')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
