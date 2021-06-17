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

from projects.models import Project

class IndexView(View):
    def get(self, request) :
        template = 'landing/index_dark.html'
        mode_version = request.GET.get('mode', None)
        if mode_version == "light" :
            template = 'landing/index_light.html'
        return render(request, template,  { 'projects' : Project.objects.all() })
    
class ContactView(View):
    def get(self, request) :
        template = 'landing/contact_dark.html'
        light_version = request.GET.get('light', None)
        if light_version == "1" :
            template = 'landing/contact_light.html'

        context = {
            'projects' : Project.objects.all()
        }
        return render(request, template, context)
    def post(self, request):
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        number = request.POST.get('number', None)
        message = request.POST.get('message', None)
        solution = request.POST.get('solution', None)

        project = get_object_or_404(Project, reference=solution)

        html_message = f"""
            <b>Name :</b> {name}
            <b>Phone :</b> {number}
            <b>Email :</b> {email}
            <b>Project # :</b> {project.reference}
            <b>Project Slogan :</b> {project.slogan}
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
    template = 'landing/solution_dark.html'
    def get(self, request) :
        mode_version = request.GET.get('mode', None)
        if mode_version == "light" :
            template = 'landing/solution_light.html'

        project_reference = request.GET.get('project') 
        return render(request, self.template, { 'project' : get_object_or_404(Project, reference=project_reference, deleted=False) })
