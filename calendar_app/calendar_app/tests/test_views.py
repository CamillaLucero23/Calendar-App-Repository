from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from calendar_app.models import *

class EventViewsTestCase(TestCase):
    def setUp(self):

        #Create a test event
        self.event = Event.objects.create(
            title="Test Event",
            description = "This is a test event",
            date = "2024-04-08",
            time="11:17:00", 
            is_active=True)
        
    def test_index_view(self):
        client = Client()
        response =client.get(reverse('index'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'calendar_app/index.html')

    def test_create_event_view(self):
        #Get form details
        client = Client()
        response = client.get(reverse('create-event'))
        self.assertEqual(response.status_code, 200)

        #Post
        data = {'title': 'Test Event',
                'description': 'This is a Test Event',
                'date' : '2024-04-08',
                'time' : '11:55:00',
                'is_active' : False }
        response = client.post(reverse('create-event'), data=data)
        self.assertEqual(response.status_code, 302)

        #Check if event was actually created
        event_count = Event.objects.filter(title='Test Event').count()
        self.assertEqual(event_count, 2)

    def test_create_event_view_invalid(self):
        client = Client()
        response = client.post(reverse('create-event'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required")

