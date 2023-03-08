from django.contrib import admin
from .models import EvenType, Event


@admin.register(EvenType)
class EvenTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'type', 'date_ini', 'date_end']