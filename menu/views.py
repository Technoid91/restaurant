from django.shortcuts import render
from .models import Food, Category


# Create your views here.

def show_menu(request):
    categories_with_food = {}

    all_categories = Category.objects.prefetch_related('food_set').all()

    for category in all_categories:
        foods_in_category = category.food_set.all()

        if foods_in_category:
            categories_with_food[category] = foods_in_category

            for food in foods_in_category:
                food.spiciness_icons = ['' for _ in range(food.spiciness)] if food.spiciness > 0 else []

    return render(request, 'menu/menu.html', {'categories': categories_with_food})
