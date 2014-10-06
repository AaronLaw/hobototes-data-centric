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
    t1 = Topic(title='  test  ', size='light', price=100)
    t2 = Topic(title=' Hello', size='medium', price=230)

    def setup(self):
        pass
    # def test_save_trim(self):
    #     """
    #     save() should return an trimmed string
    #     """
    #     test_str = '   Testing...   '
    #     test_topic = Topic(title=test_str)
    #     test_topic.save()
    #     self.assertEqual(test_topic.title, 'Testing...')

    # def test_find_packing_fee(self):
    #     # packing_fee = {'light': 3, 'medium': 5, 'heavy':8} # the key is the stored data in database: 'light', 'medium', 'heavy'
    #     # return packing_fee[self.size]
    #     t1 = Topic(title='test', size='light', price=100)
    #     self.assertEqual(t1.find_packing_fee(self), 3)

    def test_roundup(self):
        # t1 = Topic.objects.get(title='test')
        # t1 = Topic.objects.get(pk=1)

        self.assertEqual(self.t1.roundup(56, 10), 60)
        self.assertEqual(self.t1.roundup(51, 10), 60)
        self.assertEqual(self.t1.roundup(20, 10), 20)
        self.assertEqual(self.t1.roundup(21, 10), 30)
        self.assertEqual(self.t1.roundup(28, 10), 30)
        self.assertEqual(self.t1.roundup(221, 10), 230)
        self.assertEqual(self.t1.roundup(51, 100), 100)
        self.assertEqual(self.t1.roundup(151, 100), 200)


    # def test_find_postage_fee(self):
    #     t1 = Topic(title='test', size='light', price=100)
    #     self.assertEqual(t1.find_postage_fee(), 80)
