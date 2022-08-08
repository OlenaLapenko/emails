from datetime import datetime, date

from django import forms
from django.forms import DateInput


class InputForm(forms.Form):
    email = forms.EmailField()
    text = forms.CharField(max_length=200, help_text="Enter the reminder text")
    sending_time = forms.DateTimeField(required=False, widget=DateInput(attrs={'type': 'datetime-local'}),
                                       initial=datetime.now(), localize=True)
