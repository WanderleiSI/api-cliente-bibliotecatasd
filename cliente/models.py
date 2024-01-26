from django.db import models

# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=100,null=False,blank=False)
    cpf = models.CharField(max_length=11,null=False,blank=False)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.cpf