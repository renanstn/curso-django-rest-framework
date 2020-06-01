from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco


class DocIdentificacao(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacao = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, null=True, blank=True)
    imagem = models.ImageField(
        upload_to='pontos_turisticos', null=True, blank=True)
    documento_identificacao = models.OneToOneField(
        DocIdentificacao, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nome

    @property
    def descricao_completa_2(self):
        '''
        Propriedade opcional que podemos adicionar para aparecer
        no serializer
        '''
        return f"{self.nome} - {self.descricao}"
