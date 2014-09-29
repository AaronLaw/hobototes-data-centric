from django.contrib import admin

from . import models # from pickups.models import Pickup, Comment

#For Product Source
class SourceAdmin(admin.ModelAdmin):
    # fields = ['id', 'title', 'link', 'status', 'shop', 'purchase', 'ref', 'remark'] # comment out to show all fields
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
        ('Main Info',               {'fields': ['title', 'link', ]}),
        (None,               {'fields': ['status','reason', 'requirement', 'remark', 'tag', 'tags' ,'key_idea',]}),
        ('Meta Info',	 {'fields': ['seller' , 'size'], 'classes' : ['collapse']}),
        ('Price information', {'fields': ['price', 'purchase_adjectment'], 'classes' : ['collapse']}),
    ]
    inlines = [SourceInline]
    # list_display = ('title', 'id','status', 'remark', 'price', 'size', 'find_postage_fee', 'purchase_adjectment', 'max_purchase') # DEBUG. control what to be displayed in the overall admin page, instead of displaying the str()
    list_display = ('title', 'id','status', 'requirement', 'remark', 'price', 'size', 'find_max_purchase') # control what to be displayed in the overall admin page, instead of displaying the str()
    list_filter = ['seller', 'status', 'tags']
    search_fields = ['link', 'title', 'tag' ]

# For Product Category
class CategoryAdmin(admin.ModelAdmin):
# class EntryAdmin(MarkdownModelAdmin):
    list_display = ['name', 'id', 'count']
    prepopulated_fields = {'slug': ('name',  )} #[Building a blog with Django1.7 in 16 mins] (https://www.youtube.com/watch?v=7rgph8en0Jc)


# Register your models here.
admin.site.register(models.Topic, TopicAdmin)
admin.site.register(models.Source, SourceAdmin)
admin.site.register(models.Seller)
admin.site.register(models.Category, CategoryAdmin)