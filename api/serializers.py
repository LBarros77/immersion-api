from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ( Son, Botao, PlayList )

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class SonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Son
        fields = ['id', 'nome', 'url', 'duracao', 'tipo']

    def criar_son(self, dados_validados):
        self.nome = dados_validados.nome
        self.url = dados_validados.url
        self.duracao = dados_validados.duracao
        self.tipo = dados_validados.tipo
        return Son.objects.create(**dados_validados)

    def editar_son(self, instance, dados_validados):
        instance.nome = dados_validados.get('nome', instance.nome)
        instance.url = dados_validados.get('url', instance.url)
        instance.duracao = dados_validados.get('duracao', instance.duracao)
        instance.tipo = dados_validados.get('tipo', instance.tipo)
        instance.save()
        return instance


# class Botao(serializers.Serializer):
#     id = serializers.IntegerField(read_only=true)
# 	titulo = serializers.CharField()
# 	pause = serializers.BooleanField()
# 	volume = serializers.FloatField()
# 	loop = serializers.BooleanField()
# 	son = serializers.ForeignKey(Son)


# class PlayList(serializers.Serializer):
#     id = serializers.IntegerField(read_only=true)
# 	nome = serializers.CharField(maxLength=80)
# 	image_url = serializers.Charfield(maxLength=100)
# 	botao = serializers.ManyToManyField(Botao)

# 	def __str__(self):
# 		return self.nome