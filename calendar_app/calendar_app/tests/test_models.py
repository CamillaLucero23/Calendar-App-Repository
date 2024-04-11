from django.test import TestCase
from django.contrib.auth.models import User
from calendar_app.models import *

class ModelTestCase(TestCase):
    def setup(self):
        self.event = Event.objects.create(
            title="Test Event",
            description = "This is a Test Event",
            date = "4/8/2024",
            time="11:17:00", 
            is_active=True
        )
    
    def test_event_creation(self):
        self.assertEqual(self.event.title, 'Test Event')
        self.assertEqual(self.event.description, 'This is a test event')
        self.assertEqual(self.event.date, '4/8/2024')
        self.assertEqual(self.event.time, '11:17:00')
        self.assertTrue(self.event.is_active)
        self.assertEqual(str(self.event), self.event.title)
        self.assertEqual(self.event.get_absolute_url(), '/event/')