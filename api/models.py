from django.db import models


class Son(models.Model):
	nome = models.CharField(maxLength=120)
	url = models.CharField(maxLength=150)
	duracao = models.FloatField(maxLength=10)
	tipo = models.CharField(maxLength=80)

	def __str__(self):
		return self.nome


class Botao(models.Model):
	titulo = models.CharField()
	pause = models.BooleanField()
	volume = models.FloatField()
	loop = models.BooleanField()
	son = models.ForeignKey(Son)


class PlayList(models.Model):
	nome = models.CharField(maxLength=80)
	image_url = models.Charfield(maxLength=100)
	botao = models.ManyToManyField(Botao)

	def __str__(self):
		return self.nome