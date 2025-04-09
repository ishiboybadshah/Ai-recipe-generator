# generator/forms.py
from django import forms

class IngredientForm(forms.Form):
    ingredients = forms.CharField(max_length=1000)
    
