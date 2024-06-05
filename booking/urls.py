from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking, name='booking'),
    path('all/', views.admin_bookings, name='admin_bookings'),
    path('ref/<str:reference>/', views.booking_details, name='booking_details'),
    path('<reservation_id>/', views.view_booking, name='view_booking'),
    path('cancel/<reservation_id>/', views.cancel_reservation, name='cancel_reservation'),
    path('delete/<reservation_id>/', views.delete_reservation, name='delete_reservation'),

]
