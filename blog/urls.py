from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_lista, name='post_lista'),
]