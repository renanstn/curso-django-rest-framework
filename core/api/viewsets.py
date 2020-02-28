from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    # def list(self, request, *args, **kwargs):
    #     '''Método disparado no GET geral'''
    #     return Response({'teste': 123})

    # def create(self, request, *args, **kwargs):
    #     '''Método disparado no POST'''
    #     pass

    # def destroy(self, request, *args, **kwargs):
    #     '''Método disparado no DELETE'''
    #     pass

    # def retrieve(self, request, *args, **kwargs):
    #     '''Método disparado no GET de um recurso específico'''
    #     pass

    # def update(self, request, *args, **kwargs):
    #     '''Método disparado no PUT'''
    #     pass

    # def partial_update(self, request, *args, **kwargs):
    #     '''Método disparado no PATCH'''
    #     pass
