from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'description', 'status']
        error_messages = {
            'name': {
                'required': 'Name is required.',
                'max_length': 'Name cannot exceed 50 characters.',
            },
            'email': {
                'required': 'Email is required.',
                'invalid': 'Enter a valid email address.',
            },
        }