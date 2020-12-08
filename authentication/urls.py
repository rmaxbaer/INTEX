from django.urls import path
from .views import LandingView, ApplicantLoginView, ApplicantRegistrationView, OrganizationLoginView, OrganizationRegistrationView

urlpatterns = [
    path('', LandingView, name='home'),
    path('login/', ApplicantLoginView, name='login'),
    path('register/', ApplicantRegistrationView, name='register'),
    path('org/login/', OrganizationLoginView, name='org-login'),
    path('org/register/', OrganizationRegistrationView, name='org-register'),
]