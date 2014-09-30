"""
All about activity setup, e.g. sourcing campaign
"""
from django.db import models

import datetime
from django.utils import timezone
from django.contrib.sites.models import Site
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.utils.encoding import smart_str
from django.utils.translation import ugettext_lazy as _


class Campaign(models.Model):
    """
    A category of activities setup, of products.

    It indicate me when I collect that Sources for that centrin Topic.
    It has a start date and an end date.
    If it has no end date, set the end date to '0000-00-00'

    The last started campaign show first.

    A slug field is added. Idea from [Building a blog with Django1.7 in 16 mins] (https://www.youtube.com/watch?v=7rgph8en0Jc)
    """
    name = models.CharField(max_length=50, unique=True)
    # slug = models.SlugField(max_length=50, unique=True) #[Building a blog with Django1.7 in 16 mins] (https://www.youtube.com/watch?v=7rgph8en0Jc)
    created = models.DateTimeField(auto_now_add = True)
    modified= models.DateTimeField(auto_now = True)
    start_date = models.DateField()
    end_date = models.DateField(default='0000-00-00')
    remark = models.TextField(blank=True, verbose_name=_('Remark / Description'),
        help_text=_('About the sourcing campaign.'))
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return '%s' % self.name

    class Meta:
        managed =True
        verbose_name = "Campaign"
        verbose_name_plural = "Campaigns"
        ordering = ['-start_date']