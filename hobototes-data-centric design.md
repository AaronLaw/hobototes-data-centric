Documentation of Hobototes database system
=============================

### Notice board
 2014-10-01:

 I want to put the notice message in the front page of the website.
 Firstly, I think I should create an 'noticeboard' app to make it.
 Then, I think using flat page is ok for doing so.

 https://docs.djangoproject.com/en/dev/ref/contrib/flatpages/

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

