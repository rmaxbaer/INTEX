from django.shortcuts import render

# Create your views here.
def ProfileView(request):
    return render(request, 'organization/org-profile.html')

def ProfileEditView(request):
    return render(request, 'organization/org-edit-profile.html')

def ListingsView(request):
    return render(request, 'organization/org-listings.html')

def ListingView(request):
    return render(request, 'organization/org-listing.html')

def ListingCreateView(request):
    return render(request, 'organization/create-listing.html')

def ListingEditView(request):
    return render(request, 'organization/edit-listing.html')

def ApplicationView(request):
    return render(request, 'organization/org-application.html')

def ApplicationsView(request):
    return render(request, 'organization/org-applications.html')

def OffersView(request):
    return render(request, 'organization/org-offers.html')

def OfferView(request):
    return render(request, 'organization/org-offer.html')

def ApplicantsView(request):
    return render(request, 'organization/org-users.html')

def ApplicantView(request):
    return render(request, 'organization/org-user.html')
