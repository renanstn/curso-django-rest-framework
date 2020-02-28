from rest_framework.serializers import ModelSerializer
from enderecos.models import Endereco


class EnderecosSerializer(ModelSerializer):
    class Meta():
        model = Endereco
        fields = (
            'id',
            'rua',
            'bairro',
            'cidade',
            'estado',
            'pais',
            'latitude',
            'longitude',
        )
