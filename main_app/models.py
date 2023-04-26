from django.db import models
from django.urls import reverse

TRY = (
    ('N', 'No'),
    ('Y', 'Yes')
)
# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=100)
    base = models.CharField(max_length=100)
    ingredients = models.TextField(max_length=350)

    def __str__(self):
            return self.name

    def get_absolute_url(self):
            return reverse('detail', kwargs={'drink_id': self.id})

class Trying(models.Model):
    date = models.DateField()
    tried = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=TRY,
    # set the default value for meal to be 'B'
    default=TRY[0][0])
    
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_try_display()} on {self.date}"

    