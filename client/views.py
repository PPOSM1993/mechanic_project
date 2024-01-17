from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import re
# Create your views here.

def Home(request):
    return render(request, 'home.html')

def Clients(request):
    if request.method == "GET":
        clients_list = Client.objects.all()
        return render(request, 'clients.html', {'clients': clients_list})
    
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carros = request.POST.getlist('carro')
        placas = request.POST.getlist('placa')
        anos = request.POST.getlist('ano')

        clients = Client.objects.filter(cpf=cpf)

        if clients.exists():
            return render(request, 'clients.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'carros': zip(carros, placas, anos) })

        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            return render(request, 'clients.html', {'nome': nome, 'sobrenome': sobrenome, 'cpf': cpf, 'carros': zip(carros, placas, anos)})

        clients = Client(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf
        )

        clients.save()

        for carro, placa, ano in zip(carros, placas, anos):
            car = Car(carro=carro, placa=placa, ano=ano, client=clients)
            car.save()

        return render(request, 'home.html')    