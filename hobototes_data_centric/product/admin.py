from django.contrib import admin

from . import models # from pickups.models import Pickup, Comment

class TopicAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'link', 'status', 'remark', 'key_idea',]}),
        ('Meta Info',	 {'fields': ['seller' , 'size'], 'classes' : ['collapse']}),
        # ('Price information', {'fields': ['price', 'purchase_adjectment'], 'classes' : ['collapse']}),
        ('Price information', {'fields': ['price', ], 'classes' : ['collapse']}),
    ]
    # inlines = [CompetitorSourceInline]
    # list_display = ('title', 'id','status', 'remark', 'price', 'size', 'find_postage_fee', 'find_max_purchase', 'max_purchase') # DEBUG. control what to be displayed in the overall admin page, instead of displaying the str()
    # list_display = ('title', 'id','status', 'remark', 'price', 'size', 'find_max_purchase') # control what to be displayed in the overall admin page, instead of displaying the str()
    list_display = ('title', 'id','status', 'remark', 'price', 'size',) # control what to be displayed in the overall admin page, instead of displaying the str()
    list_filter = ['seller', 'status']
    search_fields = ['link', 'title']



# Register your models here.
admin.site.register(models.Topic, TopicAdmin)