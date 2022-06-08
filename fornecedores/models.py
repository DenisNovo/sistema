from django.db import models

# Create your models here.
class fornecedores(models.Model):

  empresa = models.CharField(max_length=100)
  endereco = models.CharField(max_length=100)
  cnpj = models.IntegerField(max_length=100)
  email = models.CharField(max_length=100)
  produtos = models.CharField(max_length=100)

  def str(self):
   return self.nome