from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_menu, name='menu'),
    path('add_category/', views.add_category, name='add_category'),
    path('rename_category/<int:category_id>/', views.rename_category, name='rename_category'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('add_food/', views.add_food, name='add_food'),
    path('edit_food/<int:food_id>/', views.edit_food, name='edit_food'),
    path('delete_food/<int:food_id>/', views.delete_food, name='delete_food'),
]
