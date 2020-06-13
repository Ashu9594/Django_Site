from django.db import models

# Create your models here.
class Category(models.Model):
    # id : int by default django provides id 
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.TextField()
    img = models.ImageField(upload_to="pics")

