from django.shortcuts import render

# Create your views here.


def post_lista(request):
    return render(request, 'blog/post_lista.html', {})
