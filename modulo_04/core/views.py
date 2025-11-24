from django.shortcuts import render, redirect, get_object_or_404
<<<<<<< HEAD
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as login_auth, logout as logout_auth
from django.contrib.auth.decorators import login_required

=======
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
>>>>>>> 8361ff563b2aebb49a2a88ef28b8370f15ab371f
from .models import Tarefa
from .forms import TarefaForm


<<<<<<< HEAD
# 🔐 HOME PROTEGIDA
=======
# --- CADASTRO DE USUÁRIO ---
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)  # Login automático após cadastro
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Tarefa
from .forms import TarefaForm

# --- CADASTRO DE USUÁRIO ---
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


# --- HOME ---
>>>>>>> 8361ff563b2aebb49a2a88ef28b8370f15ab371f
@login_required
def home(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.user = request.user
            tarefa.save()
            return redirect('home')
    else:
        form = TarefaForm()

<<<<<<< HEAD
    tarefas = Tarefa.objects.filter(user=request.user).order_by('-criada_em')

    context = {
        'nome_usuario': request.user.username,
        'tarefas': tarefas,
        'form': form
    }
    return render(request, 'home.html', context)


# ✔ Concluir tarefa
=======
    tarefas = Tarefa.objects.filter(user=request.user)

    return render(request, 'home.html', {
        'form': form,
        'tarefas': tarefas,
        'nome_usuario': request.user.username,
    })


# --- CONCLUIR TAREFA ---
>>>>>>> 8361ff563b2aebb49a2a88ef28b8370f15ab371f
@login_required
def concluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user)
    if request.method == 'POST':
        tarefa.concluida = True
        tarefa.save()
        return redirect('home')


<<<<<<< HEAD
# ✔ Deletar tarefa
=======
# --- DELETAR TAREFA ---
>>>>>>> 8361ff563b2aebb49a2a88ef28b8370f15ab371f
@login_required
def deletar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('home')
<<<<<<< HEAD


# 👤 Tela de Cadastro (REGISTER)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login_auth(request, user)   # login automático
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


# 👤 Tela de Login
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login_auth(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


# 🚪 Logout
@login_required
def logout(request):
    logout_auth(request)
    return redirect('login')
=======
>>>>>>> 8361ff563b2aebb49a2a88ef28b8370f15ab371f
