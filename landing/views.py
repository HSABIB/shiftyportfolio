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

        context = {
            'solutions' : Project.objects.all()
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

class SolutionsView(View):
    template = 'landing/solutions.html'
    def get(self, request) :
        context = {
            'solutions' : Project.objects.all()
        }
        return render(request, self.template, context)

class SolutionView(View):
    template = 'landing/solution.html'
    def get(self, request, *args, **kwargs) :
        solution_reference= kwargs.get('solution_reference')
        context = { 'solution' : get_object_or_404(Project, reference=solution_reference) }
        return render(request, self.template, context)
