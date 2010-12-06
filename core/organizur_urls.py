#coding=utf-8
"""


"""

from __future__ import unicode_literals
from core.utils.urls import direct
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

__all__ = ('urlpatterns',)

#==============================================================================
# Static Pages
#==============================================================================
urlpatterns = patterns('',
    direct(r'^faq/?$', 'core/faq.html', 'faq'),
    direct(r'^privacy-policy/?$', 'core/privacy-policy.html', 'privacy'),
    direct(r'^terms-of-service/?$', 'core/terms-of-service.html', 'tos'),
)

#==============================================================================
# Core
#==============================================================================
urlpatterns += patterns('organizur.core.views',
   url(r'^/?$', 'home', name = 'home'),
   url(r'^settings/?$', 'settings', name = 'settings'),
)

#==============================================================================
# Authentication Pages
#==============================================================================
urlpatterns += patterns('',
    url(r'^logout/?$', 'django.contrib.auth.views.logout', {'next_page': '/'},
        name = 'logout'),
)
