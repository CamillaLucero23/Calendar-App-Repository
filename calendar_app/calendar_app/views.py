from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views import generic

# Create your views here.

def index(request):
    return render( request, 'calendar_app/index.html')

class EventListView(generic.ListView):
    model=Event

class EventDetailView(generic.DetailView):
    model=Event

#------------------------------------------------------------------------------------------
#Forms & Such

def create_event(request):
    form = EventForm()
  
    if request.method == 'POST':
        #create a new dictionary with form data
        event_data = request.POST.copy()
        form = EventForm(event_data)

        if form.is_valid():
            #Save form without committing
            event = form.save(commit=False)
            event.save()

            #redirect
            return redirect('event')
    
    context = {'form': form}
    return render(request, 'calendar_app/create_event.html', context)


def update_event(request, pk):
    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)
  
    if request.method == 'POST':
        #create a new dictionary with form data
        event_data = request.POST.copy()
        form = EventForm(event_data, instance=event)

        if form.is_valid():
            #Save form without committing
            event = form.save(commit=False)
            event.save()

            #redirect
            return redirect('event-detail', event.id)
    
    context = {'form': form}
    return render(request, 'calendar_app/update_event.html', context)

def delete_event(request, pk):
    event = Event.objects.get(id=pk)
  
    if request.method == 'POST':
        
        #delete form if post
        event.delete()

        #redirect
        return redirect('event')
    
    context = {'event' : event}
    return render(request, 'calendar_app/delete_event.html', context)
