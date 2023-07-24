from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    address = models.CharField(max_length=100)
    image = models.ImageField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name