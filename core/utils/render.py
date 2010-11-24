#coding=utf-8
"""


"""

from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render_to_response
from functools import wraps

__all__ = ()

def render(render_func, **render_kwargs):
    """
    

    """

    def decorator(func):

        @wraps(func)
        def wrapper(request, *args, **kwargs):
            context = func(request, *args, **kwargs) or {}

            if isinstance(context, HttpResponse):
                return context

            context, headers = (context if isinstance(context, tuple) else
                                (context, {}))

            response = render_func(request, context, **render_kwargs)

            for header, value in headers.iteritems():
                response[header] = value

            return response

        return wrapper

    return decorator

def html(template):
    """
    

    """

    def render_func(request, context, **render_kwargs):
        return render_to_response(template, context)

    return render(render_func)
