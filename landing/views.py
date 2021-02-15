from django.shortcuts import render, redirect, get_object_or_404
from django.utils.html import escapejs
from django.contrib import messages
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

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
    def post(self, request):
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        number = request.POST.get('number', None)
        message = request.POST.get('message', None)

        send_mail(
            'Shifty project',
            message,
            'killersabib@gmail.com',
            ['hsabib@protonmail.com'],
            fail_silently=False,
        )
        return redirect('/contact/?msg_sent=true')
