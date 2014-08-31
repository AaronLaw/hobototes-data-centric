from django.db import models

import datetime
from django.utils import timezone
from django.contrib.sites.models import Site
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.utils.encoding import smart_str
from django.utils.translation import ugettext_lazy as _

# for find_max_purchase
from decimal import *
# getcontext().prec=6

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

    # the draft version
    # def find_max_purchase(self):
    #     USD2RMB = 6.20
    #     USD2HKD = 7.75

    #     #In USD
    #     price = float(self.price) # need type casting
    #     ebay_commision = price * 0.1
    #     paypal_commision = price * (0.039) + 0.3
    #     packing = 1.2
    #     first_leg = 16/7.75 #HKD16 to USD
    #     second_leg = 150/7.75 # HKD150 to USD
    #     max_purchase = price - (ebay_commision + paypal_commision + packing + first_leg + second_leg)
    #     return u'USD %2f,  RMB %f2' %(max_purchase, max_purchase * USD2RMB)


    # The second leg fee used in find_max_purchase()
    # https://docs.python.org/2/tutorial/datastructures.html#dictionaries
    def find_postage_fee(self): # REMEMBER: size -> weight
        postage_fee = {'light': 80, 'medium': 120, 'heavy':173} # the key is the stored data in database: 'light', 'medium', 'heavy'
        if self.size == '': # prevents bag with no size, lead to calculation error in the admin
            self.size == 'medium'
        return postage_fee[self.size]

    def find_first_leg_fee(self): # REMEMBER: size -> weight
        first_leg = {'light': 10, 'medium': 16, 'heavy': 16}
        return first_leg[self.size]

    # Work in the same way as the arithmetic that people learn at school.
    # By using Decimal instead of float
    # Google: python float vs decimal
    # https://docs.python.org/2/library/decimal.html
    def find_max_purchase(self):
        getcontext().prec=6 # Decimal.getcontext().prec
        USD2RMB = Decimal('6.20')
        USD2HKD = Decimal('7.75')

        #In USD
        price = Decimal(self.price) # str to Decimal
        ebay_commision = price * Decimal('0.10')
        paypal_commision = price *  Decimal('0.039') + Decimal('0.30')
        packing = Decimal('1.20')
        # first_leg = Decimal('16')/USD2HKD #HKD16 to USD
        first_leg = (self.find_first_leg_fee())/USD2HKD #HKD16 to USD
        # second_leg =  Decimal('173')/USD2HKD # HKD150 to USD
        second_leg = (self.find_postage_fee())/USD2HKD
        additional_fee = Decimal('1.00')
        max_purchase = price - (ebay_commision + paypal_commision + packing + first_leg + second_leg + additional_fee) 
        
        return u'US %s,  RMB %s' %(format(max_purchase, '0.2f'), format(max_purchase * USD2RMB, '0.2f') )


    class Meta:
        managed = True
        verbose_name = "Product Topic"
        verbose_name_plural = "Product Topics"
        ordering = ['id']
        # db_table = 'product_topic'

class Source(models.Model):
    STATUS = (
        ('inbox', 'inbox'),
        ('reject', 'reject'),
        ('approved', 'approved'),
        ('bought', 'bought'),
        ('watch list', 'watch list'),
        ('expired', 'expried'), # https://gist.github.com/Nagyman/9502133
        )
    # 2014-08-02
    COMMENTS = (
        ('bad', 'bad'),
        ('ok', 'seems ok'),
        ('good', 'Good!'),
        )

    SERIES = (
        ('Fashionable', 'Fashionable'),
        ('Home & Garden', 'Home & Garden'),
        ('Not-another series', 'Not-another series'),
        )

    TYPES = (

        )

    # id = models.IntegerField(primary_key=True)  # AutoField
    date = models.DateField(auto_now_add = True)
    modified= models.DateTimeField(auto_now = True)
    link = models.URLField()
    title = models.CharField(max_length=1000, blank=True)
    topic = models.ForeignKey('topic', default=25) # defautl=25 is a virtual topic
    shop = models.CharField(max_length=50, blank=True, help_text='25 means this product is a virtual product.')
    series = models.CharField(max_length=16, choices=SERIES)
    types = models.CharField(max_length=16, blank=True, null=True)
    tags = models.CharField(max_length = 50, blank=True, help_text='Use COMMA in ENGLISH to separate, not a Chinese comma')
    purchase = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    min_quantity = models.PositiveIntegerField(blank=True, default=1, help_text='The starting quantity of purchase')
    min_purchase = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, 
        help_text='The possible lowest purchase.')
    quantity_of_min_purchase = models.PositiveIntegerField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True)
    acceptability = models.CharField(max_length=4, blank=True, choices=COMMENTS, 
        help_text='A reference from buyers\' comments (aka. The product quality). Help to make decision on buy it or not. "Good" does not mean to buy')
    # status = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS, default='inbox', help_text='The workflow. Make decision to buy it or not')
    ref = models.TextField(verbose_name=_("The way it was found"), blank=True)
    # # is_good_product
    # # is_available

    def __str__(self):              # __unicode__ on Python 2
        return u'%s' % self.id
 
    class Meta:
        managed = True
        verbose_name = "Source"
        verbose_name_plural = "Sources"
        ordering = ['-modified']
        # db_table = 'competitor_sources'