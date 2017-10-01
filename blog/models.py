from django.db import models
from django.utils import timezone

# Create your models here.


class Publicacao(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=255)
    resumo = models.TextField(blank=True, null=True)
    texto = models.TextField()
    data_publicacao = models.DateTimeField(
        blank=True, null=True)

    def publicacao(self):
        self.data_publicacao = timezone.now()
        self.save()
