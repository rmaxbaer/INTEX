from django.urls import path
from .views import (
    OrgProfileView,
    OrgProfileEditView,
    OrgListingsView,
    OrgListingView,
    OrgListingEditView,
    OrgListingCreateView,
    OrgApplicationsView,
    OrgApplicationView,
    OrgOffersView,
    OrgOfferView,
    OrgApplicantsView,
    OrgApplicantView
)

urlpatterns = [
    path('', OrgProfileView, name='org-profile'),
    path('edit/', OrgProfileEditView, name='org-edit-profile'),
    path('listings/', OrgListingsView, name='org-listings'),
    path('listings/<int:listing_id>/', OrgListingView, name='org-listing'),
    path('listings/create/', OrgListingCreateView, name='org-listing-create'),
    path('listings/<int:listing_id>/edit/', OrgListingEditView, name='org-listing-edit'),
    path('applications/', OrgApplicationsView, name='org-applications'),
    path('applications/<int:application_id>', OrgApplicationView, name='org-application'),
    path('offers/', OrgOffersView, name='org-offers'),
    path('offers/<int:offer_id>/', OrgOfferView, name='org-offer'),
    path('users/', OrgApplicantsView, name='org-users'),
    path('users/<str:username>/', OrgApplicantView, name='org-user'),
]
