from django.db import models
from django.db.models import Model



# Create your models here.
class Post(models.Model):
    user = models.CharField(max_length=20, default='NULL')
    image = models.ImageField(upload_to='images/', default='NULL')
    time = models.DateTimeField()
    text = models.CharField(max_length=100, default='NULL')



