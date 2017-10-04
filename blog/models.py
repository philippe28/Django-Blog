from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField

# Create your models here.


class Publicacao(models.Model):
    autor = models.ForeignKey('auth.User')
    slug = models.SlugField(max_length=100)
    titulo = models.CharField(max_length=255)
    resumo = models.TextField(blank=True, null=True, max_length=200)
    texto = RichTextField()
    data_publicacao = models.DateTimeField(
        blank=True, null=True)

    """    image = models.ImageField(
        'Imagem', upload_to='publicacao', blank=True, null=True
    )"""

    image = models.CharField(max_length=255, blank=True, null=True)
    image_detalhe = models.CharField(max_length=255, blank=True, null=True)

    def publicacao(self):
        self.data_publicacao = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('post_detalhe', kwargs={'slug': self.slug})

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'
        ordering = ['-data_publicacao']


class Contato(models.Model):
    email = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    ip = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    data_hora = models.DateTimeField('Criado em', auto_now_add=True, null=True)

    def contato(self):
        self.save()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
