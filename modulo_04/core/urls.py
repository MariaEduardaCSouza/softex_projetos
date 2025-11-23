from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # URLs DINÂMICAS
    path('tarefa/<int:pk>/concluir/', views.concluir_tarefa, name='concluir_tarefa'),
    path('tarefa/<int:pk>/deletar/', views.deletar_tarefa, name='deletar_tarefa'),
]
