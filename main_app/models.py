from django.db import models

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=100)
    base = models.CharField(max_length=100)
    ingredients = models.TextField(max_length=350)

    def __str__(self):
        return self.name