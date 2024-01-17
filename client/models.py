from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Client(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    #cpf_regex = RegexValidator(
    #    regex=r'^0*(\d{1,3}(\.?\d{3})*)\-?([\dkK])$', message="Wrong DNI.")
    
    cpf = models.CharField(max_length=12, unique=True, verbose_name='DNI')
    #validators=[cpf_regex],
    def __str__(self):
        return self.nome

class Car(models.Model):
    #carro_regex = RegexValidator(
    #    regex=r'/^[A-ZÑ]{3}\d{3}$/', message="Wrong Patent.")
    carro = models.CharField(max_length=150)
    placa = models.CharField(max_length=8)
    ano = models.IntegerField()
    client = models.ForeignKey(Client, on_delete = models.CASCADE)
    laavgens = models.IntegerField(default=0)
    consertos = models.IntegerField(default=0)
    
    def __str__(self):
        return self.carro