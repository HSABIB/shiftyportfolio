from django.urls import path

from landing.views import IndexView, ContactView, SolutionsView, SolutionView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('solutions/', SolutionsView.as_view(), name="solutions"),
    path('solution/<str:solution_reference>', SolutionView.as_view(), name="solution"),
]