from django.contrib import admin
#from guardian.admin import GuardedModelAdmin
# Register your models here.
from .models import *

admin.site.register(Event)
admin.site.register(Calendar)
