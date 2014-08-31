from django.db import models

import datetime
from django.utils import timezone
from django.contrib.sites.models import Site
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.utils.encoding import smart_str
from django.utils.translation import ugettext_lazy as _

# for QuerySet()
from django.core.urlresolvers import reverse

# Create your models here.

# class EntryQuerySet(models.QuerySet): #[Building a blog with Django1.7 in 16 mins] (https://www.youtube.com/watch?v=7rgph8en0Jc)

#     def published(self):
#         return self.filter(publish=True)

# class Entry(models.Model):
#     title = models.CharField(max_length=200)
#     body = models.TextField()
#     slug = models.SlugField(max_length=200, unique=True)
#     publish = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)

#     objects = EntryQuerySet.as_manager()

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = "Blog Entry"
#         verbose_name_plural = "Blog Entries"
#         ordering = ["-created"]

class Topic(models.Model): #Topic

    WEIGHT_CHOICE = (
        ('light', 'Light'),
        ('medium', 'Medium'),
        ('heavy', 'Heavy'),
        )
    STATUS = (
        ('new', 'new'),
        ('in progress', 'in progress'),
        ('resloved', 'resloved'),
        ('closed', 'closed'),
        ('rejected', 'rejected'),
        )
    # id = models.IntegerField(primary_key=True)  # AutoField
    # weight = models.CharField(max_length=10, blank=True)
    create_date = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    size = models.CharField(max_length=10, blank=True, 
                                                choices=WEIGHT_CHOICE, default='medium')
    seller= models.IntegerField(default=1, help_text='#1 reserves for virtual seller.')
    # seller= models.ForeignKey('Seller', default=0)
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=250,  blank=True)
    status = models.CharField(max_length=16, choices=STATUS, default='new')
    tag = models.CharField(max_length = 50, blank=True, help_text='Use COMMA in ENGLISH to separate, not a Chinese comma')
    # is_virtual_product = # build for a themetic product grouping
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    # purchase_adjectment = models.DecimalField(max_digits=6, decimal_places=2, default=0) #TODO
    key_idea = models.TextField(blank=True, help_text='Use | to separate ideas')
    remark = models.CharField(max_length=255, blank=True, verbose_name=_('Remark / Description /Features'))

    def __str__(self):              # __unicode__ on Python 2
        return u'%s. %s (USD %d)' %(self.id, self.title, self.price,)

    class Meta:
        managed = True
        verbose_name = "Product Topic"
        verbose_name_plural = "Product Topics"
        ordering = ['id']
        # db_table = 'product_topic'