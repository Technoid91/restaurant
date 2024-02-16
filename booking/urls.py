from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking, name='booking'),
    path('ref/<str:reference>/', views.booking_details,
         name='booking_details'),

]
