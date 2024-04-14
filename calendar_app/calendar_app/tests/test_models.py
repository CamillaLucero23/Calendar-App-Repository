from django.test import TestCase
from django.contrib.auth.models import User
from calendar_app.models import *

class EventModelTestCase(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(username='TestUser', password='testuser')

        self.calendar = Calendar.objects.create(
            
        )

        self.member = Member.objects.create(
            first_name = "Test",
            last_name = "User",
            user = self.user,
            calendar = self.calendar

        )

    
        self.event = Event.objects.create(
            title="Test Event",
            description = "This is a test event",
            date = "2024-04-08",
            time="11:17:00", 
            is_active=True
        )
    
    def test_event_creation_pass(self):
        self.assertEqual(self.event.title, 'Test Event')
        self.assertEqual(self.event.description, 'This is a test event')
        self.assertEqual(self.event.date, '2024-04-08')
        self.assertEqual(self.event.time, '11:17:00')
        self.assertTrue(self.event.is_active)
        self.assertEqual(str(self.event), self.event.title)
        self.assertEqual(self.event.get_absolute_url(), 'calendar/1/event/1')
    
    def test_event_creation_fail(self):
        self.assertEqual(self.event.title, 'Test Event')
        self.assertEqual(self.event.description, '')
        self.assertEqual(self.event.date, '2024-04-08')
        self.assertEqual(self.event.time, '11:17:00')
        self.assertTrue(self.event.is_active)
        self.assertEqual(str(self.event), self.event.title)
        self.assertEqual(self.event.get_absolute_url(), 'calendar/1/event/1')
        