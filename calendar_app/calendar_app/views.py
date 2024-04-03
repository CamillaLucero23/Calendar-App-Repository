from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import generic

# Create your views here.

def index(request):
    return render( request, 'calendar_app/index.html')

class EventListView(generic.ListView):
    model=Event

class EventDetailView(generic.DetailView):
    model=Event
