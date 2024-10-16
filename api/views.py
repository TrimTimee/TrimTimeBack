# api/views.py

from rest_framework import viewsets
from .models import Cliente, Servico, Agendamento
from .serializers import ClienteSerializer, ServicoSerializer, AgendamentoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

    @action(detail=False, methods=['get'])
    def por_periodo(self, request):
        data_inicio = request.query_params.get('data_inicio')
        data_fim = request.query_params.get('data_fim')
        if data_inicio and data_fim:
            agendamentos = Agendamento.objects.filter(data__range=[data_inicio, data_fim])
        else:
            agendamentos = Agendamento.objects.all()
        serializer = self.get_serializer(agendamentos, many=True)
        return Response(serializer.data)
