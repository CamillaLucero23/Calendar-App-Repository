from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'date_time', 'is_active')