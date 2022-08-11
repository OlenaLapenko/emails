from django import forms
from django.forms import DateInput
from django.core.exceptions import ValidationError


class InputForm(forms.Form):
    email = forms.EmailField()
    text = forms.CharField(max_length=200, help_text="Enter the reminder text")
    sending_time = forms.DateTimeField(required=False, widget=DateInput(attrs={'type': 'datetime-local'}),
                                       localize=True)

    def clean_data(self):
        email = self.cleaned_data['email']
        if "fred@example.com" not in email:
            raise ValidationError("You have forgotten about Fred!")
        return email
