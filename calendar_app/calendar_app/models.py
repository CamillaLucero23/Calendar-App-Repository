from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Calendar(models.Model):

    #Model Methods
    #Gets the name of the event and uses that for their display on /admin
    def __str__(self):
        return self.title
    
    #Gets URL to access instance of model
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('calendar-detail', args=[str(self.id)])

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE) #connects user to calendars
    calendar = models.OneToOneField(Calendar,null=True, on_delete=models.CASCADE)

class Event(models.Model):

    #Model Variables
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    is_active = models.BooleanField(default=False)
    calendar = models.ForeignKey(Calendar, null=True, on_delete=models.CASCADE) #Many Events Per Calendar

    #Model Methods
    #Gets the name of the event and uses that for their display on /admin
    def __str__(self):
        return self.title
    
    #Gets URL to access instance of model
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('event-detail', args=[str(self.id)])


