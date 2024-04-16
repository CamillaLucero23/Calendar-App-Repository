from django.contrib import admin
from guardian.admin import GuardedModelAdmin
# Register your models here.
from .models import *

@admin.register(Event)
class EventAdmin(GuardedModelAdmin):
    list_display = ('title',)


@admin.register(Calendar)
class CalendarAdmin(GuardedModelAdmin):
    list_display = ('title',)