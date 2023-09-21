from django.db import models

class Post(models.Model):
    titulo_post = models.CharField(max_length=100)
    descricao_post = models.CharField(max_length=255)
    data_post = models.DateTimeField('Data publicado')
    img = models.ImageField(upload_to = 'uploads', default='')

