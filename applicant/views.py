from django.shortcuts import render
from .models import Applicant, Skill, Application
from organization.models import Organization, Listing, Offer

# Create your views here.
def ProfileView(request, username):
    pass

def ProfileEditView(request, username):
    pass

def ListingsView(request, username):
    applicant = Applicant.objects.filter(username=username)

    context = {
        'username':username,
        'applicant':applicant,
        'listings':Listing.objects.all()
    }
    return render(request, 'applicant/listings.html', context)

def ListingView(request, username):
    pass

def ApplicationView(request, username):
    pass

def ApplicationsView(request, username):
    applicant=Applicant.objects.filter(username=username)[0]

    context = {
        'username':username,
        'applicant':applicant,
        'applications':Application.objects.filter(applicant=applicant)
    }
    return render(request, 'applicant/applications.html', context)

def OffersView(request, username):
    applicant=Applicant.objects.filter(username=username)[0]
    applications = Application.objects.filter(applicant=applicant)

    context = {
        'username':username,
        'applicant':applicant,
        'offers':Offer.objects.filter(application__in=applications)
    }
    return render(request, 'applicant/offers.html', context)

def OfferView(request, username):
    pass

def OrganizationView(request, username):
    pass

def OrganizationsView(request, username):
    applicant=Applicant.objects.filter(username=username)[0]

    context = {
        'username':username,
        'applicant':applicant,
        'organizations':Organization.objects.all()
    }
    return render(request, 'applicant/organizations.html', context)