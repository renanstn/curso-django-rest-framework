from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao', 'endereco__rua')
    # lookup_field = 'nome'  # Este campo substitui o id pelo nome da url

    def get_queryset(self):
        '''Método que sobrescreve o queryset default da classe'''
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)

        queryset = PontoTuristico.objects.filter(aprovado=True)

        if id:
            queryset = queryset.filter(id=id)
        if nome:
            queryset = queryset.filter(nome__iexact=nome)  #__ieact ignora maiusc/minusc
        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)  #__ieact ignora maiusc/minusc

        return queryset

    def list(self, request, *args, **kwargs):
        '''Método disparado no GET geral'''
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        '''Método disparado no POST'''
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        '''Método disparado no DELETE'''
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        '''Método disparado no GET de um recurso específico'''
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        '''Método disparado no PUT'''
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        '''Método disparado no PATCH'''
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['get'], detail=True) # detail=True torna a PK acessível
    def denunciar(self, request, pk=None):
        '''Action personalizada, pode ser acessada com: /pontoturistico/1/denunciar/'''
        return Response({'id':pk})

    @action(methods=['get'], detail=False)
    def teste(self, request, pk=None):
        '''Action personalizada, pode ser acessada com: /pontoturistico/teste/'''
        return Response({'helo': 'world'})
