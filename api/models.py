from django.db import models


class Son(models.Model):
	nome = models.CharField(maxLength=120)
	url = models.CharField(maxLength=150)
	duracao = models.FloatField(maxLength=10)
	tipo = models.CharField(maxLength=80)

	def __str__(self):
		return self.nome


class PlayList(models.Model):
	titulo = models.CharField(maxLength=80)
	son = models.ManyToManyField()

	def __str__(self):
		return titulo