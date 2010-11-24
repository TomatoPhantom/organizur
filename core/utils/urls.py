# coding=utf-8
"""


"""

from __future__ import unicode_literals
from django.conf.urls.defaults import url

__all__ = ()

def direct(regex, template, name = None, **kwargs):
    kwargs['template'] = template

    return url(regex, 'django.views.generic.simple.direct_to_template', kwargs,
               name)
