from django.shortcuts import render, redirect, get_object_or_404
from django.utils.html import escapejs
from django.contrib import messages
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


class IndexView(View):
    def get(self, request) :
        template = 'landing/index_dark.html'
        light_version = request.GET.get('light', None)
        if light_version == "1" :
            template = 'landing/index_light.html'
        return render(request, template)
    
class ContactView(View):
    def get(self, request) :
        template = 'landing/contact_dark.html'
        light_version = request.GET.get('light', None)
        if light_version == "1" :
            template = 'landing/contact_light.html'
        return render(request, template)
