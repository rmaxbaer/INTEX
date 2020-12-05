from django.urls import path
from .views import (
    ProfileView,
    ProfileEditView,
    ListingsView,
    ListingView,
    ListingEditView,
    ListingCreateView,
    ApplicationsView,
    ApplicationView,
    OffersView,
    OfferView,
    ApplicantsView,
    ApplicantView
)

urlpatterns = [
    path('', ProfileView, name='org-profile'),
    path('edit/', ProfileEditView, name='org-edit-profile'),
    path('listings/', ListingsView, name='org-listings'),
    path('listings/<int:listing_id>/', ListingView, name='org-listing'),
    path('listings/create/', ListingCreateView, name='org-listing-create'),
    path('listings/<int:listing_id>/', ListingEditView, name='org-listing-edit'),
    path('applications/', ApplicationsView, name='org-applications'),
    path('applications/<int:application_id>', ApplicationView, name='org-application'),
    path('offers/', OffersView, name='org-offers'),
    path('offers/<int:offer_id>/', OfferView, name='org-offer'),
    path('users/', ApplicantsView, name='org-users'),
    path('users/<str:username>/', ApplicantView, name='org-user'),
]
