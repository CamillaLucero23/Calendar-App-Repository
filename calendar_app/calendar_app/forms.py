from django.forms import ModelForm, TextInput, SelectDateWidget , TimeInput, CheckboxInput
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ('first_name', 'last_name')

        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'First Name',
                }),
            
            'last_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Last Name (Optional)',
                }),
        }

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'date', 'time', 'is_active')

        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Title',
                }),

            'description': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px',
                'placeholder': 'Description'
                }),

            'date' : SelectDateWidget(attrs={
                'class': "form-control", 
                'style': 'max-width: 100px;'
                }),

            'time' : TimeInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': '00:00:00'

            }),

            'is_active': CheckboxInput(attrs={
                
            }),
            
        }   

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']