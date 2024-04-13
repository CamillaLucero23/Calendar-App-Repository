from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.index, name='index'), #Home page
    path('calendar/', views.CalendarListView.as_view(), name='calendar'), #Calendar List
    path('calendar/<int:pk>', views.CalendarDetailView.as_view(), name = 'calendar-detail'),
    path('calendar/<int:calendar_id>/event/<int:pk>', views.EventDetailView.as_view(), name='event-detail'), #Event Details
    path('calendar/<int:pk>/create-event', views.create_event, name='create-event'), # Create Event Form
    path('calendar/<int:calendar_id>/event/<int:pk>/update-event', views.update_event, name='update-event'), #Update Event Form
    path('calendar/<int:calendar_id>/event/<int:pk>/delete-event', views.delete_event, name='delete-event'), #Delete Event Form

    #user accounts
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.registerPage, name='register-page'),
    path('user/', views.userPage, name='user-page')

    ]

