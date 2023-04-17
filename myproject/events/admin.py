from django.contrib import admin
from .models import Events,Participants
# Register your models here.
class EventsAdmin(admin.ModelAdmin):
    list_display=['event_name','description','starts_at','ends_at','venue']

class ParticipantsAdmin(admin.ModelAdmin):
    list_display=['user','event_name','is_registered']

admin.site.register(Events,EventsAdmin)
admin.site.register(Participants,ParticipantsAdmin)