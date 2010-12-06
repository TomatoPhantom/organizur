#coding=utf-8
"""


"""

from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

__all__ = ()

class RedirectSocialLoginMiddleware(object):
    """


    """

    __ERROR_MESSAGES = ('error: facebook', 'error: openid', 'error: oauth',
                        'error: inactive_account')

    def process_response(self, request, response):
        """"""

        if any(response.content == error for error in self.__ERROR_MESSAGES):
            return HttpResponseRedirect(reverse('organizur.core.home'))

        return response

