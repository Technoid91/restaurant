from django import forms
from .models import Category, Food


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class FoodForm(forms.ModelForm):
    SPICINESS_CHOICES = [(i, i) for i in range(6)]

    spiciness = forms.ChoiceField(
        choices=SPICINESS_CHOICES,
        widget=forms.Select,
        help_text='0 - not spicy, 5 - extremely spicy'
    )

    class Meta:
        model = Food
        fields = '__all__'
