from django.test import TestCase
from django.contrib.auth.models import User
from calendar_app.forms import *

class EventFormTestCase(TestCase):

    def test_valid_case(self):
        data = {'title': 'Event Title',
                'description': 'This is a Test Event',
                'date' : '2024-04-08',
                'time' : '11:55:00',
                'is_active' : False }
        
        form = EventForm(data=data)
        self.assertTrue(form.is_valid())

    def test_missing_title(self):
        print("False Form Test")
        data = {'title': '',
                'description': 'This is a Test Event',
                'date' : '2024-04-08',
                'time' : '11:55:00',
                'is_active' : False }
        
        form = EventForm(data=data)
        self.assertFalse(form.is_valid()) 
        self.assertIn('title', form.errors)



