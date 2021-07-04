from django.urls import path

from landing.views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('services/', ServicesView.as_view(), name="services"),
    path('works/', WorksView.as_view(), name="works"),
    path('about-us/', AboutView.as_view(), name="about"),
    path('project/', SolutionView.as_view(), name="solution"),

    path('service/developement/', DevelopementView.as_view(), name="developement"),
    path('service/design-graphique/', DeisgnView.as_view(), name="design"),
    path('service/cloud-devops/', DevopsView.as_view(), name="devops"),
    path('service/support/', SupportView.as_view(), name="support"),
]