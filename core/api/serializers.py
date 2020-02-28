from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracoesSerializer
from enderecos.api.serializers import EnderecosSerializer
from comentarios.api.serializers import ComentariosSerializer
from avaliacoes.api.serializers import AvaliacoesSerializer


class PontoTuristicoSerializer(ModelSerializer):

    atracoes = AtracoesSerializer(many=True)
    endereco = EnderecosSerializer()
    comentarios = ComentariosSerializer(many=True)
    avaliacao = AvaliacoesSerializer(many=True)

    class Meta:
        model = PontoTuristico
        fields = (
            'id',
            'nome',
            'descricao',
            'aprovado',
            'atracoes',
            'comentarios',
            'avaliacao',
            'endereco',
            'imagem',
        )
