from django import forms

from .models import Event, Registration


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['student_id', 'student_name', 'student_whatsapp_number']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student_id'].label = "Your Student ID"
        self.fields['student_name'].label = "Your name"
        self.fields['student_whatsapp_number'].label = "Your Whatsapp Number"
