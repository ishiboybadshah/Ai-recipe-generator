from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import IngredientForm
from .utils import generate_recipe
from datetime import datetime

def home(request):
    recipe = None
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredients = form.cleaned_data['ingredients']
            recipe = generate_recipe(ingredients)
    else:
        form = IngredientForm()
    
    return render(request,'home.html',context={'form': form, 'recipe': recipe,
        'year': datetime.now().year})
