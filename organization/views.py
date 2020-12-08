from django.shortcuts import render
from .models import Listing, Organization, Offer
from applicant.models import Application, Applicant, Skill

# Create your views here.
def OrgProfileView(request, organization_name):
    organization=Organization.objects.filter(username=organization_name)[0]
    
    context = {
        'organization_name':organization_name,
        'organization':organization
    }    
    return render(request, 'organization/org-profile.html', context)

def OrgProfileEditView(request, organization_name):
    organization=Organization.objects.filter(username=organization_name)[0]
    
    context = {
        'organization_name':organization_name,
        'organization':organization
    }
    return render(request, 'organization/org-edit-profile.html', context)

def OrgListingsView(request, organization_name):
    organization=Organization.objects.filter(username=organization_name)[0]
    
    context = {
        'organization_name':organization_name,
        'organization':organization,
        'listings':Listing.objects.filter(organization=organization)
    }
    return render(request, 'organization/org-listings.html', context)

def OrgListingView(request, organization_name, listing_id):
    organization=Organization.objects.filter(username=organization_name)[0]
    listing=Listing.objects.filter(id=listing_id)[0]
    
    context = {
        'organization_name':organization_name,
        'organization':organization,
        'listing':listing
    }
    return render(request, 'organization/org-listing.html', context)

def OrgListingCreateView(request, organization_name):
    organization=Organization.objects.filter(username=organization_name)[0]
    
    context = {
        'organization_name':organization_name,
        'organization':organization
    }
    return render(request, 'organization/create-listing.html', context)

def OrgListingEditView(request, organization_name, listing_id):
    organization=Organization.objects.filter(username=organization_name)[0]
    listing=Listing.objects.filter(id=listing_id)[0]
    
    context = {
        'organization_name':organization_name,
        'organization':organization,
        'listing':listing
    }
    return render(request, 'organization/edit-listing.html', context)

def OrgApplicationView(request, organization_name, application_id):
    organization=Organization.objects.filter(username=organization_name)[0]
    application=Application.objects.filter(id=application_id)[0]
    
    context = {
        'organization_name':organization_name,
        'organization':organization,
        'application':application
    }
    return render(request, 'organization/org-application.html', context)

def OrgApplicationsView(request, organization_name):
    organization=Organization.objects.filter(username=organization_name)[0]
    listings=Listing.objects.filter(organization=organization)
    
    context = {
        'organization_name':organization_name,
        'organization':organization,
        'applications':Application.objects.filter(listing__in=listings)
    }
    return render(request, 'organization/org-applications.html', context)

def OrgOffersView(request, organization_name):
    organization=Organization.objects.filter(username=organization_name)[0]
    
    context = {
        'organization_name':organization_name,
        'organization':organization,
        'offers':Offer.objects.filter(organization=organization)
    }
    return render(request, 'organization/org-offers.html', context)

def OrgOfferView(request, organization_name, offer_id):
    organization=Organization.objects.filter(username=organization_name)[0]
    offer=Offer.objects.filter(id=offer_id)[0]

    context = {
        'organization_name':organization_name,
        'organization':organization,
        'offer':offer
    }
    return render(request, 'organization/org-offer.html', context)

def OrgApplicantsView(request, organization_name):
    organization=Organization.objects.filter(username=organization_name)[0]
    
    context = {
        'organization_name':organization_name,
        'organization':organization,
        'applicants':Applicant.objects.all()
    }
    return render(request, 'organization/org-users.html', context)

def OrgApplicantView(request, organization_name, username):
    organization=Organization.objects.filter(username=organization_name)[0]
    applicant=Applicant.objects.filter(username=username)
    
    context = {
        'organization_name':organization_name,
        'organization':organization,
        'applicant':applicant
    }
    return render(request, 'organization/org-user.html', context)
