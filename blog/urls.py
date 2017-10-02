from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_lista, name='post_lista'),
    url(r'^post/(?P<slug>[\w_-]+)/$', views.post, name='post_detalhe'),
	url(r'^/contato', views.post, name='contato'),
]
