from django.contrib import admin
from .models import New
# Register your models here.


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'text')
