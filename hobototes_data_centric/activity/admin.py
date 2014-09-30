from django.contrib import admin

from . import models # from pickups.models import Pickup, Comment

#For Product Source
class CampaignAdmin(admin.ModelAdmin):
    # fields = ['id', 'title', 'link', 'status', 'shop', 'purchase', 'ref', 'remark'] # comment out to show all fields
    list_display = ('id', 'name', 'start_date', 'end_date', 'created', 'modified') # control what to be displayed in the overall admin page, instead of displaying the str()
    list_filter = ['name']
    search_fields = ['name']

# Register your models here.
admin.site.register(models.Campaign, CampaignAdmin)
