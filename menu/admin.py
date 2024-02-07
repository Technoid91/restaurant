from django.contrib import admin
from .models import Category, Food

# Registering Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Registering Food model
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'vegan', 'spiciness')
    list_filter = ('category', 'vegan')