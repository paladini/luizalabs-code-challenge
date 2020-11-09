from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Client(models.Model):

    class Meta:
        db_table = 'clients'

    name = models.TextField(max_length=200)
    email = models.EmailField(max_length=200, unique=True, db_index=True)
    
    favorites = models.ManyToManyField('Product', through='FavoriteList')

    def __str__(self):
        return self.name
    
class Product(models.Model):

    class Meta:
        db_table = 'products'

    price = models.CharField(max_length=50)
    image = models.CharField(max_length=2048) # max chars that an URL can have
    brand = models.CharField(max_length=200, db_index=True)
    title = models.CharField(max_length=200, db_index=True)
    review_score = models.DecimalField(max_length=200, decimal_places=2, max_digits=10)
    
    favorited = models.ManyToManyField('Client', through='FavoriteList')

    def __str__(self):
        return self.title
    
    
class FavoriteList(models.Model):

    client = models.ForeignKey(Client, on_delete = models.CASCADE, related_name="clients")
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name="products")
    
    class Meta:
        db_table = 'favorites_list'
        unique_together = ('client', 'product',)