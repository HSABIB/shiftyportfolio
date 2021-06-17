from django.urls import path

from landing.views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('project/', SolutionView.as_view(), name="solution"),
]