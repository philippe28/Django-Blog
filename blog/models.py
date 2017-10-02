from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField

# Create your models here.


class Publicacao(models.Model):
    autor = models.ForeignKey('auth.User')
    slug = models.SlugField(max_length=100)
    titulo = models.CharField(max_length=255)
    resumo = models.TextField(blank=True, null=True)
    texto = RichTextField()
    data_publicacao = models.DateTimeField(
        blank=True, null=True)

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
