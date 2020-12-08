from django.shortcuts import render

# Create your views here.
def LandingView(request):
    return render(request, 'authentication/landing.html')

def ApplicantLoginView(request):
    return render(request, 'authentication/login.html')
    

def ApplicantRegistrationView(request):
    return render(request, 'authentication/register.html')
    

def OrganizationLoginView(request):
    return render(request, 'authentication/login.html')

def OrganizationRegistrationView(request):
    return render(request, 'authentication/register.html')

