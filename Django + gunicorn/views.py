# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template.loader import render_to_string #для render_to_string


from urlparse import urlparse

# Create your views here.

from django.views.generic import TemplateView
from django.http import HttpResponse

class AboutView(TemplateView):
    template_name = "about.html"

def index(request):
    return render(request, "index.html", {})

def register(request):
    return render(request, "register.html", {})

def hello(request):
    return render(request, "hello.html", {
        'title': 'Hello, bro',
        'text': 'Rustam the best',
    })

def get_post(request):
    if request.method=='GET':
        return render(request, "get_post.html", {
            'method': request.method,
            'parameters': request.GET,
            'value': request.GET.values(),
        })
    else:
        return render(request, "get_post.html", {
            'method': request.method,
            'parametres': request.POST,
        })