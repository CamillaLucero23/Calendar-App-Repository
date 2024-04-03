from django.db import models
from django.urls import reverse

# Create your models here.

class Event(models.Model):

    #Model Variables
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    date_time = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    #Model Methods
    #Gets the name of the event and uses that for their display on /admin
    def __str__(self):
        return self.title
    
    #Gets URL to access instance of model
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('event-detail', args=[str(self.id)])
