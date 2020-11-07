from django.db import models

class Client(models.Model):

    class Meta:

        db_table = 'clients'

    name = models.TextField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return self.name