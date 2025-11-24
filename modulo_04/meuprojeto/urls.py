from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),

    path('tarefa/<int:pk>/concluir/', views.concluir_tarefa, name='concluir_tarefa'),
    path('tarefa/<int:pk>/deletar/', views.deletar_tarefa, name='deletar_tarefa'),
]