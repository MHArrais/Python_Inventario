from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Produto

# View para login
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_itens') # <- Redirecionar para a página de lista de itens
        else:
            return render(request, 'login.html',{'error': 'Credenciais inválidas'})
        
    return render(request, 'login.html')

# View para cadastrar itens (VISUALIZADO APENAS PARA USUARIOS LOGADOS)
@login_required

def cadastrar_item(request):
    if request.method == "POST":
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        ano = request.POST['ano']
        preco = request.POST['preco']
        Produto.objects.create(marca=marca, modelo=modelo, ano=ano, preco=preco)
        return redirect('lista_itens') # Redirecionar para a mesma página depois de cadastrar
    return render(request, 'cadastrar_item.html')

# Função para verificar os produtos cadastrado em uma página após o registro
@login_required
def lista_itens(request):
    # Busca todos os produtos cadastrados no banco de dados
    produtos = Produto.objects.all()

    #Renderiza o template e passa a lista de veículos
    return render(request, 'lista_itens.html', {'produtos': produtos})

# View para o usuário criar uma conta para acesso.

def registrar_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Loga automaticamente o usuário após o registro
            login(request, user)
            return redirect('lista_itens') # Redireciona para a lista de itens
    else:
        form = UserCreationForm()
    
    return render(request, 'registrar.html', {'form': form})

def logout_login(request):
    logout(request)
    return redirect('lista_itens')