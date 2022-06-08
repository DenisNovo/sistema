from django.db import models

# Create your models here.

class clientes(models.Model):

    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    idade = models.IntegerField(max_length=100)
    cpf = models.IntegerField(max_length=100)

    def str(self):
        return self.nome