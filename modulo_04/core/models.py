from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    concluida = models.BooleanField(default=False)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo
