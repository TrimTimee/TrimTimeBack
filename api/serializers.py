# api/serializers.py

from rest_framework import serializers
from datetime import datetime
from .models import Cliente, Servico, Agendamento

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'

    def validate(self, data):
        agendamentos = Agendamento.objects.filter(data=data['data'])
        for agendamento in agendamentos:
            inicio_existente = datetime.combine(agendamento.data, agendamento.hora_inicio)
            fim_existente = datetime.combine(agendamento.data, agendamento.hora_fim)
            novo_inicio = datetime.combine(data['data'], data['hora_inicio'])
            novo_fim = datetime.combine(data['data'], data['hora_fim'])
            if (inicio_existente < novo_fim and novo_inicio < fim_existente):
                raise serializers.ValidationError("Conflito de horário com outro agendamento.")
        return data
