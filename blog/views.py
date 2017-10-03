from django.shortcuts import render
from django.utils import timezone
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

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
    
    form = ContatoForm(request.POST or None)
    if form.is_valid():
		
			
        contato = form.save(commit=False)
        contato.nome = request.POST.get('nome', '')
        contato.email = request.POST.get('email', '')
		
        contato.save()

    return render(request, 'blog/contato.html')
	
def landing(request):
    
    form = ContatoForm(request.POST or None)
    if form.is_valid():
	
        contato = form.save(commit=False)
        contato.nome = request.POST.get('nome', '')
        contato.email = request.POST.get('email', '')
		
        contato.save()

    return render(request, 'blog/landing.html')

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