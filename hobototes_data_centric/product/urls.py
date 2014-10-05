from django.conf.urls import url

from product import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<topic_id>[0-9]+)/$', views.detail, name='detail'),

]