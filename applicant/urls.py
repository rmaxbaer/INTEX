from django.urls import path
from .views import (
    ProfileView,
    ProfileEditView,
    ListingsView,
    ListingView,
    ApplicationsView,
    ApplicationView,
    OffersView,
    OfferView,
    OrganizationsView,
    OrganizationView
)

urlpatterns = [
    path('profile/', ProfileView, name='profile'),
    path('profile/edit/', ProfileEditView, name='profile-edit'),
    path('listings/', ListingsView, name='listings'),
    path('listings/<int:listing_id>/', ListingView, name='listing'),
    path('applications/', ApplicationsView, name='applications'),
    path('applications/<int:application_id>/', ApplicationView, name='application'),
    path('offers/', OffersView, name='offers'),
    path('offers/<int:offer_id>/', OfferView, name='offer'),
    path('employers/', OrganizationsView, name='employers'),
    path('employers/<str:organization_name>', OrganizationView, name='employer'),
]