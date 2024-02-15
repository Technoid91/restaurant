import uuid
from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .models import Table, Reservation
from .forms import ReservationForm


def booking(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            party_size = form.cleaned_data['party_size']
            date = form.cleaned_data['date']
            time_str = form.cleaned_data['time']
            time = datetime.strptime(time_str, '%H:%M').time()
            date_time = datetime.combine(date, time)
            date_time = timezone.make_aware(date_time)

            current_datetime = timezone.now()
            if date_time <= current_datetime:
                form.add_error(None, "Дата и время бронирования должны быть больше текущей даты и времени.")
                return render(request, 'booking/booking-template.html', {'form': form})

            start_time = date_time - timedelta(hours=1, minutes=59)
            end_time = date_time + timedelta(hours=1, minutes=59)

            existing_reservations = Reservation.objects.filter(
                date_time__range=(start_time, end_time)
            )
            all_tables = Table.objects.all()
            reserved_tables = Table.objects.filter(reservation__in=existing_reservations)
            available_tables = all_tables.exclude(pk__in=reserved_tables.values_list('pk', flat=True))

            available_tables = available_tables.order_by('capacity')

            assigned_tables = []
            if party_size > 0:
                while party_size > 0 and available_tables.exists():
                    largest_table = available_tables.last()
                    for table in available_tables:
                        if table.capacity >= party_size:
                            assigned_tables.append(table)
                            party_size = 0
                            break
                    if party_size > 0:
                        assigned_tables.append(largest_table)
                        party_size = party_size - largest_table.capacity
                        available_tables = available_tables.exclude(pk=largest_table.pk)
                if party_size == 0:

                    new_reservation = form.save(commit=False)
                    new_reservation.date_time = date_time
                    new_reservation.reference = str(uuid.uuid4())[:8]
                    new_reservation.save()
                    new_reservation.table_number.set(assigned_tables)
                    form.save_m2m()

                    messages.add_message(
                        request, messages.SUCCESS,
                        'Reservation successfully created.'
                    )
                    return redirect(f'ref/{new_reservation.reference}')
                else:

                    messages.error(request, 'Sorry, no tables available for the requested amount of people')
                    form.add_error(None, "Sorry, no tables available for the requested amount of people")
    else:
        form = ReservationForm()

    return render(request, 'booking/booking.html', {'form': form})


def booking_details(request, reference):
    reservation = get_object_or_404(Reservation, reference=reference)
    return render(request, 'booking/booking_details.html', {'reservation': reservation})





