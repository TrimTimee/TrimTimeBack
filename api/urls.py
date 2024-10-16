# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, ServicoViewSet, AgendamentoViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'servicos', ServicoViewSet)
router.register(r'agendamentos', AgendamentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
