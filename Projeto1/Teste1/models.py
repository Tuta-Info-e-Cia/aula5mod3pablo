from django.db import models

# Create your models here.
class Cliente(models.Model):

    nome =  models.CharField(max_length=50)

    cpf =  models.IntegerField() 

    rg =  models.IntegerField()

    email =  models.TextField()

    telefone =  models.IntegerField()

    endereco =  models.TextField()

    data_nascimento =  models.DateField()

    sexo =  models.CharField(max_length=50)

    ativo = models.BooleanField(default=50)

    criado_em =  models.DateTimeField(auto_now_add=50)

    atualizado_em =  models.DateTimeField(auto_now=50)