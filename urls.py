#coding=utf-8
"""


"""

from __future__ import unicode_literals
from django.conf import settings
from django.conf.urls.defaults import handler404 as default_404_handler
from django.conf.urls.defaults import handler500 as default_500_handler
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin
from staticfiles.urls import staticfiles_urlpatterns

__all__ = ('urlpatterns', 'handler404', 'handler500')

#==============================================================================
# Error Pages
#==============================================================================
handler404 = default_404_handler
handler404 = default_500_handler

#==============================================================================
# Admin Tool
#==============================================================================
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls))
)

#==============================================================================
# Apps
#==============================================================================
urlpatterns += patterns('',
    (r'^', include('organizur.core.urls')),
    (r'^(?P<username>\w+)/imgur/?',
     include('organizur.imgur.urls', namespace = 'imgur', app_name = 'imgur')),
    (r'^(?P<username>\w+)/projects/?',
     include('organizur.projects.urls', namespace = 'projects',
             app_name = 'projects')),
    (r'^(?P<username>\w+)/surveys/?',
     include('organizur.surveys.urls', namespace = 'surveys',
             app_name = 'surveys')),
)

#==============================================================================
# Static Files
#==============================================================================
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
