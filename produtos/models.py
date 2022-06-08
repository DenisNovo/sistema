from django.db import models

# Create your models here.
class produtos(models.Model):

    sapatos = models.CharField(max_length=100)
    camisetas = models.CharField(max_length=100)
    calcas = models.CharField(max_length=100)
    chapeus = models.CharField(max_length=100)
    shorts = models.CharField(max_length=100)

    def str(self):
        return self.nome