from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hobototes_data_centric.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
)


# for flatpages
# see: https://docs.djangoproject.com/en/dev/ref/contrib/flatpages/
# from django.contrib.flatpages import views
# urlpatterns += (
#     url(r'^(?P<url>.*/)$', views.flatpage),
#     # url(r'^about-us/$', views.flatpage, {'url': '/about-us/'}, name='about'),
#     # url(r'^license/$', views.flatpage, {'url': '/license/'}, name='license'),
# )
