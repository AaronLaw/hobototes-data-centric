from django.conf.urls import url

from product import views

urlpatterns = [
    # ex: /polls/
    # url(r'^$', views.index, name='index'),
    # url(r'^(?P<topic_id>[0-9]+)/$', views.detail, name='detail'),
    # convert to generic views
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]