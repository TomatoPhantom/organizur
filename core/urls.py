#coding=utf-8
"""


"""

from __future__ import unicode_literals
from core.utils.urls import direct
from django.conf import settings
from django.conf.urls.defaults import handler404 as default_404_handler
from django.conf.urls.defaults import handler500 as default_500_handler
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin
from staticfiles.urls import staticfiles_urlpatterns

__all__ = ('urlpatterns', 'handler404', 'handler500')

handler404 = default_404_handler
handler404 = default_500_handler
admin.autodiscover()

urlpatterns = patterns('',
    direct(r'^faq/?$', 'core/faq.html', 'organizur.core.faq'),
)

urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^(?P<username>\w+)/imgur/?', include('organizur.imgur.urls')),
    (r'^(?P<username>\w+)/projects/?', include('organizur.projects.urls')),
    (r'^(?P<username>\w+)/surveys/?', include('organizur.surveys.urls')),
)

urlpatterns += patterns('organizur.core.views',
   url(r'^/?$', 'home', name = 'organizur.core.home')
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
