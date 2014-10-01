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

# for trim the leading & ending whitespace
from django.core.exceptions import ValidationError


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
    end_date = models.DateField(default='0001-01-01', 
        help_text=_('Set to 0001-01-01 for non-ending campagin'))
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

    def save(self,  *args,  **kwargs):
        '''
        Override the save() method, in order to trim the starting & ending whitespace in a title

        ref: Google: django super save -> https://docs.djangoproject.com/en/1.7/topics/db/models/ -> the "Overriding predefined model methods" section
        '''
        # test if I can override the save()
        # self.name = 'aaron'
        # super(Campaign, self).save(*args, **kwargs) # Call the "real" save() method.
        
        # the actual code that trims whitespace
        # ref: Google: trim string -> http://stackoverflow.com/questions/5043012/django-trim-whitespaces-from-charfield
        try:
            self.name = self.name.strip()
            raise ValidationError('The whitespace is trimmed.')
        except ValidationError as e:
            print(e)

        super(Campaign, self).save(*args, **kwargs) # Call the "real" save() method.