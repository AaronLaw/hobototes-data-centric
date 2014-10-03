Documentation of Hobototes database system
=============================

### Calculation on x-leg fee

2014-10-03:
We need a more precious calculation on the postage fee.
Since we've got a formular from post office, we can calculate the exact postage fee now.
We've to refine the weight of a product, not just put it into 3 categories.

For example, ship to US:
<50g: $16
51~100g: $21
101~500g: +$1.1
501~2000g: +1.0

That is,

1st_boundary = 16
2nd_boundary = 21
3rd_boundary = 21+(500-100)/10 * 1.1
STEP = 10g

if weight <=50:
    return 16 #HKD
elif weight <=100:
    return 21
elif weight <=500:
    2nd_boundary + ((weight -100) /  STEP ) * 1.1 
elif weight <=2000:
    3rd_boundary + ((weight-500) / STEP) * 1.0
else
    Cannot ship. Need to find another solution

Now, I go to round the weight to nearest 10g (included). Don't forget the r fee is $15.5

2014-09-13:

in 10g increment.

2nd leg fee should be made of 2 parts: the exact product weight, and the weight of packing.

2014-09-30:

After a deep thinking:
The calculation of 2nd leg fee in the Product Topic should not be precise. For example: An apple cutter we'got is made of plastic. One day later, I've found an apple cutter of the same shape made of steel. So, how to determent the weight of THAT apple cutter in THAT TOPIC? (plastic vs steel)

Therefore, I intend to put the calculation in SKU model also.

2014-08:
The postage fee is roughly calculated.
It is based on the weight of the product:  {'light': 80, 'medium': 120, 'heavy':173}.
When the `size` is 'light', then the fee is $80.


### Notice board
 2014-10-01:

 I want to put the notice message in the front page of the website.
 Firstly, I think I should create an 'noticeboard' app to make it.
 Then, I think using flatpages is ok for doing so.

 https://docs.django project.com/en/dev/ref/contrib/flatpages/

### Comments should be related to many models, rather than bind to only one model

2014-06-20:
The 'comments' model can link to one and only one model. (e.g. once I've linked 'comments' to 'Topic', it cannot be linked to another model like 'shoppings')

Google: django many one to many tables

[2014-06-24: ContentType maybe the solution. https://docs.djangoproject.com/en/1.5/ref/contrib/contenttypes/#django.contrib.contenttypes.generic.GenericForeignKey,  from: http://django-contrib-comments.readthedocs.org/en/latest/models.html
when I Google: Django comment system
]

### Status of Produce source

Product source
=====
2014-04-16
inbox
rejected
approved | Watchlist
bought
expired

### Short sell

short sell: (2014-06-16:)
======
objective: to enrich the stock
operative: As it takes at least 3 days no transferring the product from Taobao to us, it is risky for short term listing. Fees may increased from Manybo consolidation.
Considering:
GTC/Fixed Price: It enrich our stock, but can't ship the product to customer immediately. RISKY!
Auction: We need to buy the short sell product immediately when it takes the 1st bid, as it takes 3+ days to transfer to HK. Therefore, the longer the auction, the more safety. (However, the sell through of 10-day-auction is not good as the 7-day-auction's.)

Benefit: 1. Enrich the stock/SKU 2. Test before buy in.
Cons: Risky of no product at hand, losing of 1 day processing of our promise.

Implementation: @see the Short_sell table in Bags source v2.6.ods

SKU, start_date, stautus[just select|draft|approved (list on ebay already)], Listing format, Tag[draft;short sell|approved;short sell], Next Action[Watch it everyday|Forget it|Need to buy]

4 Status of short sell
------------------------
just select - short sell in pickup table
draft;shortsell - still in datasheet & desc ready
approved;shortsell - still in datasheet & image ready
approved;shortsell - already listing

