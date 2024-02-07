from django.urls import path
from .views import show_menu

app_name = 'menu'

urlpatterns = [
    path('', show_menu, name='menu'),  # URL для страницы с меню
    # Дополнительные URL-адреса вашего приложения могут быть добавлены здесь
]