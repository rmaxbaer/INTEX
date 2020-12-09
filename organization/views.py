from django.shortcuts import render, redirect
from django.db.models import Value as V
from django.db.models.functions import Concat 
from .models import Listing, Organization, Offer
from applicant.models import Application, Applicant, Skill

# Create your views here.
def OrgProfileView(request, organization_name):
    organization=Organization.objects.filter(username=organization_name)[0]
    listings=Listing.objects.filter(organization=organization)
    number_of_listings=listings.count()
    
    context = {
        'organization_name':organization_name,
        'organization':organization,
        'number_of_listings':number_of_listings
    }    
    return render(request, 'organization/org-profile.html', context)

def OrgProfileEditView(request, organization_name):
    organization=Organization.objects.filter(username=organization_name)[0]
    
    context = {
        'organization_name':organization_name,
        'organization':organization,
        'date_founded':str(organization.date_founded)
    }

    if request.method == 'POST':
        organization.company_name = request.POST['company_name']
        organization.email = request.POST['email']
        organization.phone_number = request.POST['phone_number']
        organization.address = request.POST['address']
        organization.city = request.POST['city']
        organization.state = request.POST['state']
        organization.zip = request.POST['zip']
        organization.size = request.POST['size']
        organization.sectors = request.POST['sectors']
        organization.description = request.POST['description']
        organization.date_founded = request.POST['date_founded']
        try :
            organization.profile_picture = request.FILES['profile_picture']
        except :
            pass
        try :
            organization.cover_picture = request.FILES['cover_picture']
        except :
            pass
        organization.save()
        return redirect('org-profile', organization_name)

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

    if request.method == 'POST':
        listing = Listing.objects.create(
            organization = organization,
            job_title = request.POST['job_title'],
            job_description = request.POST['job_description'],
            contract_type = request.POST['contract_type'],
            compensation = request.POST['compensation'],
            relocation_assistance = ('on' == request.POST['relocation_assistance']),
            positions_available = request.POST['positions_available'],
            location = request.POST['location'],
        )
        return redirect('org-listing', organization_name, listing.id)
    return render(request, 'organization/create-listing.html', context)

def OrgListingEditView(request, organization_name, listing_id):
    organization=Organization.objects.filter(username=organization_name)[0]
    listing=Listing.objects.filter(id=listing_id)[0]
    
    context = {
        'organization_name':organization_name,
        'organization':organization,
        'listing':listing
    }
    if request.method == 'POST':
        listing.organization = organization
        listing.job_title = request.POST['job_title']
        listing.job_description = request.POST['job_description']
        listing.contract_type = request.POST['contract_type']
        listing.compensation = request.POST['compensation']
        listing.relocation_assistance = ('on' == request.POST['relocation_assistance'])
        listing.positions_available = request.POST['positions_available']
        listing.location = request.POST['location']
        listing.save()
        return redirect('org-listing', organization_name, listing.id)

    return render(request, 'organization/edit-listing.html', context)

def OrgApplicationView(request, organization_name, application_id):
    organization=Organization.objects.filter(username=organization_name)[0]
    application=Application.objects.filter(id=application_id)[0]
    
    context = {
        'organization_name':organization_name,
        'organization':organization,
        'application':application
    }
    if request.method == 'POST':
        if request.POST['submit'] == 'decline':
            application.status = 'declined'
            application.save()
            return redirect('org-applications', organization_name)
        elif request.POST['submit'] == 'accept':
            application.status = 'accepted'
            offer = Offer.objects.create(
                application = application,
                deadline = request.POST['deadline'],
                start_date = request.POST['start_date'],
                compensation = request.POST['compensation'],
                message = request.POST['message']
            )
            return redirect('org-offer', organization_name, offer.id)

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
    listings = Listing.objects.filter(organization=organization)
    applications = Application.objects.filter(listing__in=listings)

    context = {
        'organization_name':organization_name,
        'organization':organization,
        'offers':Offer.objects.filter(application__in=applications)
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

    if request.method == 'POST':
        applicants = Applicant.objects.annotate(full_name=Concat('first_name', V(' '), 'last_name')).filter(full_name__icontains=request.POST['applicant_name'])
        context['applicants']=applicants

    return render(request, 'organization/org-users.html', context)

def OrgApplicantView(request, organization_name, username):
    organization=Organization.objects.filter(username=organization_name)[0]
    applicant=Applicant.objects.filter(username=username)[0]
    
    context = {
        'organization_name':organization_name,
        'organization':organization,
        'applicant':applicant,
        'username':username
    }
    return render(request, 'organization/org-user.html', context)
