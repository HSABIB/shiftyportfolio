from django.urls import path

from landing.views import IndexView, ContactView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('contact/', ContactView.as_view(), name="contact"),
]