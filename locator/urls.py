from django.conf.urls import patterns, url

from .views import locator, locations


urlpatterns = patterns('',
    url(r'^$', locator, name='locator'),
    url(r'^locations/$', locations, name='locations'),
)

