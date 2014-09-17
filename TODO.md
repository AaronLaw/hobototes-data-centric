# TODO

## Product
* [x] 2014-09-01: Topic: find max purchase
* [x] 2014-09-01:Topic: change find_max_purchase uses deciaml
* [ ] 2014-09-02: make categories as a model, rather than a list hand-coded in the Topic model.
* [ ] prepare the `category` data from the old db data: extract the existing data and insert into the new table
	insert into `product_category`(name)  SELECT DISTINCT `category` from `competitor_sources`
* [ ] 2014-09-02: use fixture to pre-popular the database
* [ ] 2014-09-01:  data reduce on Seller model: let QQ, Wechat, Address as a key-value pair, as they are not usually stored with each seller
* [ ] 2014-09-09: [華爾街之狼 所有的能力都是能被訓練的] (https://www.youtube.com/watch?v=1uUF7_svLII)
    * [ ] 2014-09-09: estmiated price (think what if it looks beautiful, and we donno the buy-in purchase)
    * [ ] 2014-09-09: market reference price
* [ ] 2014-09-12: for better manage the Product Topic: make a  marketing campign
* [ ] 2014-09-13: calculation on the 2nd leg fee (part 1 + part 2)
	* [ ] 2014-09-13: part 1: calculate by the weight of the product (in 50g step)
	* [ ] 2014-09-13: part 2: calculate by the weight of packing (in 3 steps)

## Tag
* [x] 2014-09-02: install Taggit
* [x] 2014-09-03: use Django-Taggit to tag (https://readthedocs.org/projects/django-taggit/)
* [ ] 2014-09-03: use Django-Taggit-Suggest to enchance taggit (http://django-taggit.readthedocs.org/en/latest/external_apps.html)
* [ ] 2014-09-03: remove `tag` field after the data is migrated to `tags` (which is powered by django-taggit)

## Image management
* [ ] 2014-09-08: allow upload pic to Product Topic
* [ ] find some useful image management plugin: https://readthedocs.org/projects/tags/image/

## Business Overview

[華爾街之狼 所有的能力都是能被訓練的] (https://www.youtube.com/watch?v=1uUF7_svLII)

* [ ] 2014-09-09: dashboard
* [ ] 2014-09-08: keep ratio of AUC/BIN to  3:7
    ** [ ] 2014-09-08: group by month
* [ ] 2014-09-08: eBay profit calculator

## Workflow

## Comments
https://github.com/django/django-contrib-comments

----
# Notes

2014-09-16:

Upgrade to Django 1.7

	pip install Django==1.7

2014-09-02:
### objective: 
我要把 `competitor_sources` 的 `category`copy 到 `producte_category` 去，並且最好按出現的 freq 從大到小排序（方便將來按 `id` 順序選擇時，最常用的 category name 會最先出現。）（現時是以 `name` 的順序去排序，A 在最先而 Z 在最後。）

把 `competitor_sources` 的 `category`copy 到 `producte_category` 去：

	insert into `product_category`(name)  SELECT DISTINCT `category` from `competitor_sources`
Google: insert into
http://www.w3schools.com/sql/sql_insert_into_select.asp

如何抽取到 distinct 的 category name 呢？

	SELECT  `category`, count(category) from `competitor_sources`  group by category


所以要按 freq 從大到小排序的話，就是：

	SELECT `category`, count(category) from `competitor_sources`  group by category  order by count(category) desc


按 freq 從高到低放到去 id 的做法就是：

    INSERT INTO `product_category` (name) SELECT `category`  from `competitor_sources`  group by category  order by count(category) desc



有個 freq count  的主意也不錯，所以我在 `category` model 裡加入 conunt： 

    count = models.PositiveIntegerField(default=0)


然後按 freq 從高到低放到去 id 的做法就變成是：

    INSERT INTO `product_category` (name, count) SELECT `category`, count(category)  from `competitor_sources`  group by category  order by count(category) desc

----
2014-09-13:

On design the calculation of the 2nd leg fee.

