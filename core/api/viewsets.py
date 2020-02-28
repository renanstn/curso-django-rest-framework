from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
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

    @action(methods=['get'], detail=True) # detail=True torna a PK acessível
    def denunciar(self, request, pk=None):
        '''Action personalizada, pode ser acessada com: /pontoturistico/1/denunciar/'''
        return Response({'id':pk})

    @action(methods=['get'], detail=False)
    def teste(self, request, pk=None):
        '''Action personalizada, pode ser acessada com: /pontoturistico/teste/'''
        return Response({'helo': 'world'})
