from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField
from core.models import PontoTuristico, DocIdentificacao
from enderecos.models import Endereco
from atracoes.models import Atracao
from atracoes.api.serializers import AtracoesSerializer
from enderecos.api.serializers import EnderecosSerializer
from comentarios.api.serializers import ComentariosSerializer
from avaliacoes.api.serializers import AvaliacoesSerializer

class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'


class PontoTuristicoSerializer(ModelSerializer):

    atracoes = AtracoesSerializer(many=True)
    endereco = EnderecosSerializer()
    documento_identificacao = DocIdentificacaoSerializer()
    # comentarios = ComentariosSerializer(many=True)
    # avaliacao = AvaliacoesSerializer(many=True)

    descricao_completa = SerializerMethodField()

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
            'descricao_completa',
            'descricao_completa_2',
            'documento_identificacao',
        )
        read_only_fields = ('comentarios', 'avaliacao', 'aprovado')
        # Detalhe: Campo aprovado no read_only para que o usuario nao possa
        # criar pontos pré-aprovados

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            atracao_obj = Atracao.objects.create(**atracao)
            ponto.atracoes.add(atracao_obj)
        return ponto

    def cria_endereco(self, endereco, ponto):
        endereco_obj = Endereco.objects.create(**endereco)
        ponto.endereco = endereco_obj
        return ponto

    def cria_documento(self, documento, ponto):
        documento_obj = DocIdentificacao.objects.create(**documento)
        ponto.documento_identificacao = documento_obj
        return ponto
    
    def create(self, validated_data):
        '''
        Aqui é tratado para que todos os vínculos do ponto turíscito,
        tanto as ForeignKeys quando ManyToMany sejam criados no mesmo
        momento que o post envia as informações.
        Atrações é um exemplo de ManyToMany
        Endereço é um exemplo de ForeignKey
        '''

        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        documento = validated_data['documento_identificacao']
        del validated_data['documento_identificacao']

        ponto = PontoTuristico.objects.create(**validated_data)

        self.cria_atracoes(atracoes, ponto)
        self.cria_endereco(endereco, ponto)
        self.cria_documento(documento, ponto)

        ponto.save()

        return ponto

    def get_descricao_completa(self, obj):
        """Chave adicional que podemos adicionar no serializer"""
        return f"{obj.nome} - {obj.descricao}"
