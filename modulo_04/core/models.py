from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
<<<<<<< HEAD

=======
>>>>>>> 8361ff563b2aebb49a2a88ef28b8370f15ab371f
    titulo = models.CharField(max_length=200)
    concluida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
<<<<<<< HEAD
=======

>>>>>>> 8361ff563b2aebb49a2a88ef28b8370f15ab371f
