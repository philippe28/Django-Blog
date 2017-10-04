from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_lista, name='post_lista'),
    url(r'^post/(?P<slug>[\w_-]+)/$', views.post, name='post_detalhe'),
	url(r'^contato$', views.contato, name='contato'),
	url(r'^landing$', views.landing, name='landing'),
	url(r'^ebooks/(?P<filename>)/$', views.pdf_download, 'views.pdf_download'),
]
