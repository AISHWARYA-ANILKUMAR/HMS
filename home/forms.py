from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

        widgets ={
            'booking_date': DateInput(),
        }

        labels ={

    'p_name': " PATIENT NAME ",
    'p_phone' : "PATIENT PHONE ",
    'p_email' : "PATIENT EMAIL ",
    'doc_name' : "DOCTOR NAME ",
    'booking_date' :"BOOKING DATE ",
        }
