from django import forms
from django.utils import timezone
from .models import Reservation
from datetime import datetime


class ReservationForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    TIME_CHOICES = [(f'{hour:02d}:{minute:02d}', f'{hour:02d}:{minute:02d}')
                    for hour in range(16, 21)
                    for minute in range(0, 45, 15)]

    time = forms.ChoiceField(choices=TIME_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control'})
                             )

    party_size = forms.IntegerField(min_value=1, max_value=10)

    comments = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}), required=False)

    class Meta:
        model = Reservation
        fields = ('party_size', 'date', 'time', 'first_name', 'last_name',
                  'phone_number', 'email', 'comments', )
        labels = {
            'phone_number': 'Phone',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['date'].initial = self.instance.date_time.date()
            self.fields['time'].initial = self.instance.date_time.strftime('%H:%M')

    def save(self, commit=True):
        """
        saves date and time from to fields to a single one
        in the required format
        """
        instance = super().save(commit=False)
        date = self.cleaned_data['date']
        time_str = self.cleaned_data['time']
        time = datetime.strptime(time_str, '%H:%M').time()

        datetime_without_timezone = datetime.combine(date, time)
        timezone_aware_datetime = timezone.make_aware(
            datetime_without_timezone, timezone.get_current_timezone()
        )
        instance.date_time = timezone_aware_datetime
        if commit:
            instance.save()
        return instance
