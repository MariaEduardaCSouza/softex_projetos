from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('concluir/<int:pk>/', views.concluir_tarefa, name='concluir_tarefa'),
    path('deletar/<int:pk>/', views.deletar_tarefa, name='deletar_tarefa'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    # API
    path('api/tarefas/', views.TarefaListAPIView.as_view()),
    path('api/tarefas/contagem/', views.ContagemTarefasAPIView.as_view()),
]
