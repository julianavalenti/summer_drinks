
from django.shortcuts import render

# Add the following import
from django.http import HttpResponse


# Add the Cat class & list and view function below the imports

class Drink:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, base, ingredients):
    self.name = name
    self.base = base
    self.ingredients = ingredients
    

drinks = [
  Drink('Marguerita', 'Tequila', 'marguerita recipe '),
  Drink('Bloody Mary', 'Tomate juice', 'Bloody mary recipe'),
  Drink('Sangria', 'White wine', 'Sangria recipe')
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Summer Drinks!</h1>')
def about(request):
    return render(request, 'about.html')
def drinks_index(request):
#   drinks = Drink.objects.all(),
  return render(request, 'drinks/index.html', { 'drinks': drinks })