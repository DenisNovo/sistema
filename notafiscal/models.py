from django.db import models

# Create your models here.
class notafiscal(models.Model):

    produto = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    cpf = models.IntegerField(max_length=100)
    cores = models.CharField(max_length=100)
    preco = models.IntegerField(max_length=100)

    def str(self):
        return self.nome
