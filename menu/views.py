from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Food, Category
from .forms import CategoryForm, FoodForm

# Create your views here.


def show_menu(request):
    """ Renders menu page with categories and dishes """
    categories_with_food = {}
    empty_categories = []

    all_categories = Category.objects.prefetch_related('food_set').all()

    for category in all_categories:
        foods_in_category = category.food_set.all()

        if foods_in_category:
            categories_with_food[category] = foods_in_category

            for food in foods_in_category:
                food.spiciness_icons = ['' for _ in range(food.spiciness)] \
                    if food.spiciness > 0 else []
        else:
            empty_categories.append(category)

    return render(request, 'menu/menu.html', {
        'categories': categories_with_food,
        'empty_categories': empty_categories,
    })


def add_category(request):
    """ Add new category to the menu """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added category!')
            return redirect(reverse('add_category'))
        else:
            messages.error(request, 'Failed to add new category. Please ensure the form is valid.')
    else:
        form = CategoryForm()

    template = 'menu/add_category.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def rename_category(request, category_id):
    """ Rename category """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))

    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category renamed!')
            return redirect('menu')
        else:
            messages.error(request, 'Failed to rename category. Please ensure the form is valid.')
    else:
        form = CategoryForm(instance=category)
        messages.info(request, f'You are editing {category.name}')

    template = 'menu/rename_category.html'
    context = {
        'form': form,
        'category': category,
    }

    return render(request, template, context)


def delete_category(request, category_id):
    """ Delete category from the menu """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))

    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    messages.success(request, 'category deleted!')
    return redirect(reverse('menu'))


def add_food(request):
    """ Add new dish to the menu """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added dish!')
            return redirect(reverse('menu'))
        else:
            messages.error(request, 'Failed to add new dish. Please ensure the form is valid.')
    else:
        form = FoodForm()

    template = 'menu/add_item.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def edit_food(request, food_id):
    """ Edit a dish in the menu """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))

    food = get_object_or_404(Food, pk=food_id)
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dish updated successfully!')
            return redirect('menu')
        else:
            messages.error(request, 'Failed to update dish. Please ensure the form is valid.')
    else:
        form = FoodForm(instance=food)

    template = 'menu/edit_food.html'
    context = {
        'form': form,
        'food': food,
    }
    return render(request, template, context)


def delete_food(request, food_id):
    """ Delete a dish from the menu """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))

    food = get_object_or_404(Food, pk=food_id)
    food.delete()
    messages.success(request, 'dish deleted!')
    return redirect(reverse('menu'))
