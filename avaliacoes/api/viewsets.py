from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacao
from .serializers import AvaliacoesSerializer


class AvaliacoesViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacoesSerializer
