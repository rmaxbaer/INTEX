from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from applicant.models import Applicant
from organization.models import Organization
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def LandingView(request):
    return render(request, 'authentication/landing.html')

def ApplicantLoginView(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile', username)
    return render(request, 'authentication/login.html')


def ApplicantRegistrationView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zip = request.POST['zip']
        Applicant.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            address=address,
            city=city,
            state=state,
            zip=zip
        )

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile', username)

    return render(request, 'authentication/register.html')


def OrganizationLoginView(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('org-profile', username)

    return render(request, 'authentication/login.html', {'org':True})

def OrganizationRegistrationView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        company_name = request.POST['company_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zip = request.POST['zip']

        Organization.objects.create_user(
            username=username,
            password=password,
            company_name=company_name,
            email=email,
            phone_number=phone_number,
            address=address,
            city=city,
            state=state,
            zip=zip
        )

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('org-profile', username)

    return render(request, 'authentication/org-register.html')

