from django.shortcuts import render, redirect, get_object_or_404
from django.utils.html import escapejs
from django.contrib import messages
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from projects.models import Project, Category, Service

class IndexView(View):
    def get(self, request) :
        template = 'landing/index.html'
        return render(request, template)

class WorksView(View):
    def get(self, request) :
        template = 'landing/works.html'
        return render(request, template,  { 'projects' : Project.objects.all(), 'categories': Category.objects.all() })

class ServicesView(View):
    def get(self, request) :
        template = 'landing/services.html'
        context = {
            'services': Service.objects.all()
        }
        return render(request, template, context)

class DevelopementView(View):
    def get(self, request) :
        template = 'landing/services/developement.html'
        return render(request, template)

class DeisgnView(View):
    def get(self, request) :
        template = 'landing/services/design.html'
        return render(request, template)

class DevopsView(View):
    def get(self, request) :
        template = 'landing/services/devops.html'
        return render(request, template)

class SupportView(View):
    def get(self, request) :
        template = 'landing/services/support.html'
        return render(request, template)

class AboutView(View):
    def get(self, request) :
        template = 'landing/about.html'
        return render(request, template)

class ContactView(View):
    def get(self, request) :
        template = 'landing/contact.html'
        context = {
            'projects' : Project.objects.all()
        }
        return render(request, template, context)
    def post(self, request):
        name = request.POST.get('name', None)
        number = request.POST.get('number', None)
        message = request.POST.get('message', None)

        html_message = f"""
            <b>Name :</b> {name}
            <b>Phone :</b> {number}
            <b>Message :</b> {message}
        """

        plain_message = strip_tags(html_message)

        send_mail(
            'Shifty project',
            plain_message,
            'killersabib@gmail.com',
            ['hsabib@protonmail.com'],
            fail_silently=False,
        )
        return redirect('/contact/?msg_sent=true')

class SolutionView(View):
    def get(self, request) :
        template = 'landing/solution_dark.html'
        project_reference = request.GET.get('project') 
        return render(request, template, { 'project' : get_object_or_404(Project, reference=project_reference, deleted=False) })
