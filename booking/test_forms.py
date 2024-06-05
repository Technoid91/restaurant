from django.test import TestCase
from .forms import ReservationForm


class TestBookingForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields """
        form = ReservationForm({
            'party_size': '2',
            'date': '2042-06-05',
            'time': '17:00',
            'first_name': 'Tom',
            'last_name': 'Anderson',
            'phone_number': '0443055678',
            'email': 'wakeup@zeon.com',
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")