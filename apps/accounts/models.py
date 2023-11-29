from django.db import models

class Post(models.Model):
    titulo_post = models.CharField(max_length=100)
    descricao_post = models.CharField(max_length=255)
    data_post = models.DateTimeField('Data publicado')
    img = models.ImageField(upload_to = 'uploads', default='')

class Adocao(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=20)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    motivacao = models.TextField()
    concordo = models.BooleanField()

    def __str__(self):
        return self.nome
