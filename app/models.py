from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    # dt_criacao = models.DateTimeFields(auto_)