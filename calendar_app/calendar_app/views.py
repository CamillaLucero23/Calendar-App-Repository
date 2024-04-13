from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .decorators import *
from django.views import generic

from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render( request, 'calendar_app/index.html')

class EventDetailView(generic.DetailView):
    model=Event

class CalendarListView(generic.ListView):
    model = Calendar

class CalendarDetailView(generic.DetailView):
    model = Calendar

    def get_context_data(self, **kwargs):
        #Call base implentation to get context
        context = super(CalendarDetailView, self).get_context_data(**kwargs)

        #Create data and add to context
        events = Event.objects.filter(calendar=self.get_object().id)
        context['events'] = events
        return context

#------------------------------------------------------------------------------------------
#Forms & Such

@login_required(login_url='login')
@allowed_users(allowed_roles=['user_role'])
def create_event(request, pk):
    form = EventForm()
    calendar = Calendar.objects.get(pk=pk)
    if request.method == 'POST':
        #create a new dictionary with form data
        event_data = request.POST.copy()
        event_data['calendar'] = pk
        form = EventForm(event_data)

        if form.is_valid():
            #Save form without committing
            event = form.save(commit=False)
            event.calendar = calendar
            event.save()

            #redirect
            return redirect('calendar-detail', pk)
    
    context = {'form': form}
    return render(request, 'calendar_app/create_event.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['user_role'])
def update_event(request, calendar_id, pk):
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
            return redirect('calendar-detail', pk)
    
    context = {'form': form}
    return render(request, 'calendar_app/update_event.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['user_role'])
def delete_event(request, pk, calendar_id):
    if request.user.has_perm('calendar_app.can_edit_calendar'):
        event = Event.objects.get(id=pk)
  
        if request.method == 'POST':
        
            #delete form if post
            event.delete()

            #redirect
            return redirect('event')
    
        context = {'event' : event}
        return render(request, 'calendar_app/delete_event.html', context)
    
    else:
        #redirect
            return redirect('/')


def registerPage(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            #Handle user Creation first
            user = form.save()
            group = Group.objects.get(name='user_role')
            user.groups.add(group)

            calendar = Calendar.objects.create()
            content_type = ContentType.objects.get_for_model(calendar)
            permission = Permission.objects.get(codename='can_edit_calendar', content_type=content_type)
            user.user_permissions.add(permission)

            member = Member.objects.create(user=user)
            member.calendar = calendar

            member.save()
            return redirect('login')
    
    context = {'form' : form}
    return render(request, 'registration/register.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['user_role'])
def userPage(request):
    member = request.user.member
    form = MemberForm(instance=member)
    calendar = member.calendar

    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()

    context = {'calendars':calendar, 'form':form}
    return render(request, 'calendar_app/user.html', context) 