from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'), #Home page
    path('event/', views.EventListView.as_view(), name='event'), #Event List
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event-detail'), #Event Details
    path('event/create-event', views.create_event, name='create-event'), # Create Event Form
    path('event/<int:pk>/update-event', views.update_event, name='update-event'), #Update Event Form
    path('event/<int:pk>/delete-event', views.delete_event, name='delete-event'), #Delete Event Form
    ]
