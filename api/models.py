# api/models.py

from django.db import models
from datetime import datetime

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.DurationField(help_text='Duração do serviço em horas:minutos')
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

# Definição única do modelo Agendamento
class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.hora_fim:
            duracao = self.servico.duracao
            datetime_inicio = datetime.combine(self.data, self.hora_inicio)
            datetime_fim = datetime_inicio + duracao
            self.hora_fim = datetime_fim.time()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cliente.nome} - {self.servico.nome} em {self.data} às {self.hora_inicio}"
