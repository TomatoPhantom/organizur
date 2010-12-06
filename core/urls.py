#coding=utf-8
"""


"""

from __future__ import unicode_literals
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns

__all__ = ('urlpatterns',)

#==============================================================================
# Authentication Pages
#==============================================================================
urlpatterns = patterns('',
    (r'^', include('organizur.core.organizur_urls', namespace = 'organizur',
                   app_name = 'organizur')),
    (r'^accounts/', include('socialregistration.urls')),
)
