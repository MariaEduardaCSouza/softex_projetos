from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

<<<<<<< HEAD
    # URLs DINÂMICAS
    path('tarefa/<int:pk>/concluir/', views.concluir_tarefa, name='concluir_tarefa'),
    path('tarefa/<int:pk>/deletar/', views.deletar_tarefa, name='deletar_tarefa'),
=======
    path('tarefa/<int:pk>/concluir/', views.concluir_tarefa, name='concluir_tarefa'),
# Ex: /tarefa/5/deletar/
    path('tarefa/<int:pk>/deletar/', views.deletar_tarefa, name='deletar_tarefa'),
    path('register/', views.register, name='register'),
>>>>>>> 8361ff563b2aebb49a2a88ef28b8370f15ab371f
]
