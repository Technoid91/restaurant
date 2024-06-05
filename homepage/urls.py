from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_carousel, name='home'),
    path('add/', views.add_news, name='add_news'),
    path('edit/<int:new_id>/', views.edit_news, name='edit_news'),
    path('del/<int:new_id>/', views.delete_news, name='delete_news'),
]
