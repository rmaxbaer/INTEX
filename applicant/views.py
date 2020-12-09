from django.shortcuts import render
from .models import Applicant, Skill, Application
from organization.models import Organization, Listing, Offer

# Create your views here.
def ProfileView(request, username):
    pass

def ProfileEditView(request, username):
    applicant = Applicant.objects.filter(username=username)[0]

    context = {
        'username':username,
        'applicant':applicant,
        'birth_date':str(applicant.birth_date)
    }

    if request.method == 'POST':
        applicant.first_name = request.POST['first_name']
        applicant.last_name = request.POST['last_name']
        applicant.email = request.POST['email']
        applicant.address = request.POST['address']
        applicant.city = request.POST['city']
        applicant.state = request.POST['state']
        applicant.zip = request.POST['zip']
        applicant.about_me = request.POST['about_me']
        applicant.birth_date = request.POST['birth_date']
        try :
            applicant.profile_picture = request.FILES['profile_picture']
        except :
            pass
        try :
            applicant.cover_picture = request.FILES['cover_picture']
        except :
            pass
        try :
            applicant.resume = request.FILES['resume']
        except :
            pass
        applicant.save()
        return redirect('profile', username)

    return render(request, 'applicant/profile-edit.html', context)

def ListingsView(request, username):
    applicant = Applicant.objects.filter(username=username)

    context = {
        'username':username,
        'applicant':applicant,
        'listings':Listing.objects.all()
    }
    return render(request, 'applicant/listings.html', context)

def ListingView(request, username, listing_id):
    applicant = Applicant.objects.filter(username=username)

    context = {
        'username':username,
        'applicant':applicant,
        'listing':Listing.objects.filter(id=listing_id)
    }
    return render(request, 'applicant/listing.html', context)

def ApplicationView(request, username, application_id):
    applicant = Applicant.objects.filter(username=username)

    context = {
        'username':username,
        'applicant':applicant,
        'application':Application.objects.filter(id=application_id)
    }
    return render(request, 'applicant/application.html', context)

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

def OfferView(request, username, offer_id):
    applicant = Applicant.objects.filter(username=username)

    context = {
        'username':username,
        'applicant':applicant,
        'offer':Offer.objects.filter(id=offer_id)
    }
    return render(request, 'applicant/offer.html', context)

def OrganizationView(request, username, organization_name):
    applicant = Applicant.objects.filter(username=username)

    context = {
        'username':username,
        'applicant':applicant,
        'organization':Organization.objects.filter(username=organization_name)
    }
    return render(request, 'applicant/organization.html', context)

def OrganizationsView(request, username):
    applicant=Applicant.objects.filter(username=username)[0]

    context = {
        'username':username,
        'applicant':applicant,
        'organizations':Organization.objects.all()
    }
    return render(request, 'applicant/organizations.html', context)