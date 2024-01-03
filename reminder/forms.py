from django import forms
from .models import Reminder
from .models import Medication
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['reminder_time', 'is_completed']

    reminder_time = forms.DateTimeField(
        label='Reminder Time',
        input_formats=['%Y-%m-%dT%H:%M'], 
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    )

class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['name', 'dosage', 'frequency', 'start_date']


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'Email'

    def clean_password2(self):
        
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2
