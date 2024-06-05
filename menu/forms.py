from django import forms
from .models import Category, Food


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'
