from django.db import models

class Client(models.Model):

    class Meta:

        db_table = 'clients'

    name = models.TextField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):

    class Meta:

        db_table = 'products'

    price = models.CharField(max_length=50)
    image = models.CharField(max_length=2048) # max chars that an URL can have
    brand = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    reviewScore = models.DecimalField(max_length=200, decimal_places=2, max_digits=2)

    def __str__(self):
        return self.title