from django.test import TestCase
from django.db import models
from product.models import * # import the Topic, Source, ...


import datetime
from django.utils import timezone
from django.contrib.sites.models import Site
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.utils.encoding import smart_str
from django.utils.translation import ugettext_lazy as _

# for find_max_purchase
from decimal import * # Google: django price
getcontext().prec=6

# for QuerySet()
from django.core.urlresolvers import reverse

# for taggit
from taggit.managers import TaggableManager

# for trim the leading & ending whitespace
from django.core.exceptions import ValidationError

# Create your tests here.
# ref: https://docs.djangoproject.com/en/dev/topics/testing/
class TopicTests(TestCase):
    t1 = Topic(title='  test  ', size='light', price=69.93, tag='cabas, 牛皮', weight=1200, campaign_id=1)
    t2 = Topic(title='  Hello', size='medium', price=89.93, tag='cabas, 牛皮. ', weight=875, campaign_id=2 )
    t3 = Topic.objects.get(pk=3)

    def setup(self):
        category1 = Category(name='Test Category')
        category1.save()

    # def test_save_trim(self):
    # #     """
    # #     save() should return an trimmed string
    # #     """
    #     self.t1.save()
    #     self.assertEqual(t1.title, 'test ')


    def test_roundup(self):
        # t1 = Topic.objects.get(title='test')
        # t1 = Topic.objects.get(pk=1)
        self.assertEqual(self.t1.roundup(56, 10), 60)
        self.assertEqual(self.t1.roundup(51, 10), 60)
        self.assertEqual(self.t1.roundup(20.0, 10), 20.0)
        self.assertEqual(self.t1.roundup(21.1, 10), 30.0)
        self.assertEqual(self.t1.roundup(28, 10), 30)
        self.assertEqual(self.t1.roundup(221, 10), 230)
        self.assertEqual(self.t1.roundup(51, 100), 100)
        self.assertEqual(self.t1.roundup(151, 100), 200)

    def test_find_first_leg_fee(self):
        self.assertEqual(self.t1.find_first_leg_fee(), 10)
        self.assertEqual(self.t2.find_first_leg_fee(), 16)


    def test_find_postage_fee(self):
        # t1 = Topic(title='test', size='light', price=100)
        self.assertEqual(self.t1.find_postage_fee(), Decimal(135.0) )
        self.assertEqual(self.t2.find_postage_fee(), Decimal(103.0    ) )
        t4 = Topic(title='  test  ', size='light', price=69.93, tag='cabas, 牛皮', weight=453, )
        t7 = Topic(title='  test  ', size='light', price=69.93, tag='cabas, 牛皮', weight=101, )
        t5 = Topic(title='  test  ', size='light', price=69.93, tag='cabas, 牛皮', weight=21, )
        t6 = Topic(title='  test  ', size='light', price=69.93, tag='cabas, 牛皮', weight=28, )
        t8 = Topic(title='  test  ', size='heavy', price=69.93, tag='cabas, 牛皮', weight=2800, )
        self.assertEqual(t4.find_postage_fee(), Decimal(60.6) )
        self.assertEqual(t5.find_postage_fee(), Decimal(16.0) )
        self.assertEqual(t6.find_postage_fee(), Decimal(16.0) )
        self.assertEqual(t7.find_postage_fee(), Decimal(22.1) )
        self.assertEqual(t8.find_postage_fee(), Exception() )

    def test_find_2nd_class_postage_fee(self):
        t4 = Topic(title='  test  ', size='light', price=69.93, tag='cabas, 牛皮', weight=25, )
        t7 = Topic(title='  test  ', size='light', price=69.93, tag='cabas, 牛皮', weight=101, )
        t5 = Topic(title='  test  ', size='light', price=69.93, tag='cabas, 牛皮', weight=210, )
        self.assertEqual(t4.find_2nd_class_postage_fee(), Decimal(20.5) )
        self.assertEqual(t5.find_2nd_class_postage_fee(), Decimal(42.0) )
        
        

    def test_find_packing_fee(self):
        # packing_fee = {'light': 3, 'medium': 5, 'heavy':8} # the key is the stored data in database: 'light', 'medium', 'heavy'
        # return packing_fee[self.size]
        self.assertEqual(self.t1.find_packing_fee(), 3)
        self.assertEqual(self.t2.find_packing_fee(), 5)