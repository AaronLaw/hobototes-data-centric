from django.contrib import admin

# from django.db import models
from . import models # from pickups.models import Pickup, Comment


#For Product Source
class SourceAdmin(admin.ModelAdmin):
    # fields = ['id', 'title', 'link', 'status', 'shop', 'purchase', 'ref', 'remark'] # comment out to show all fields
    fieldsets = [
        ('Main Inforamtion',               {'fields': [ 'link', 'title','shop', ]}),
        ('Price information', {'fields': ['purchase', 'min_quantity','min_purchase', 'quantity_of_min_purchase',  ], }),
        ('Relational (Grouping purpose)',               {'fields': ['topic','series', 'category' ,]}),
        ('Meta Infomation',    {'fields': ['tag', 'tags', 'remark' , 'ref' , 'acceptability' , 'status' ], }),
    ]

    list_display = ('id', 'created' , 'category', 'title', 'shop', 'purchase', 'acceptability', 'tag', 'tags')#'tag') # control what to be displayed in the overall admin page, instead of displaying the str()
    list_filter = ['status', 'series', 'category', 'tags', 'topic']
    search_fields = ['title', 'status','purchase', 'shop' ,'remark', 'tag']


# For Product Topic
class SourceInline(admin.TabularInline):
    model = models.Source
    # exclude = ('id',)
    extra = 1

class TopicAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Main Info',               {'fields': ['title', 'link', 'market_reference_price', ]}),
        (None,               {'fields': ['status','reason', 'campaign', 'requirement', 'remark', 'tag', 'tags' ,'key_idea',]}),
        ('Meta Info',	 {'fields': ['seller' , 'size'], 'classes' : ['collapse']}),
        ('Price information', {'fields': ['price', 'purchase_adjectment'], }),
    ]
    inlines = [SourceInline]
    # list_display = ('title', 'id','status', 'remark', 'price', 'size', 'find_postage_fee', 'purchase_adjectment', 'max_purchase') # DEBUG. control what to be displayed in the overall admin page, instead of displaying the str()
    list_display = ('title', 'id', 'remark',  'get_tags' ,'count_source_by_status', 'status','size', 'market_reference_price', 'price',  'find_max_purchase', 'requirement',) # control what to be displayed in the overall admin page, instead of displaying the str()
    list_filter = ['campaign',  'status', 'tags'] # campaign, not activity.campaign, as it is already imported from model
    search_fields = ['link', 'title', 'tag' ]


# For Product Category
class CategoryAdmin(admin.ModelAdmin):
# class EntryAdmin(MarkdownModelAdmin):
    list_display = ['name', 'id', 'count', 'show_count_freq']
    prepopulated_fields = {'slug': ('name',  )} #[Building a blog with Django1.7 in 16 mins] (https://www.youtube.com/watch?v=7rgph8en0Jc)


# Register your models here.
admin.site.register(models.Topic, TopicAdmin)
admin.site.register(models.Source, SourceAdmin)
admin.site.register(models.Seller)
admin.site.register(models.Category, CategoryAdmin)
