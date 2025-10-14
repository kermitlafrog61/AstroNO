from django import forms

from .models import Event, Registration


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['student_id', 'student_name']
