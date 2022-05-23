from django.contrib import admin
#from .models import APIData
from .models import APIWEB
from .models import Parameters
# Register your models here.
admin.site.register(APIWEB)
admin.site.register(Parameters)