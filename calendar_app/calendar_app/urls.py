from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'), #Home page
    path('event/', views.EventListView.as_view(), name='event'), #Event List
]
