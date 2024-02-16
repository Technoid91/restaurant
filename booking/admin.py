from django.contrib import admin
from .models import Table, Reservation

# Register your models here.


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('reference', 'date_time', 'last_name',
                    'party_size', 'get_tables')
    filter_horizontal = ('table_number',)

    def get_tables(self, obj):
        return ", ".join([str(table) for table in obj.table_number.all()])

    get_tables.short_description = 'Table Numbers'
