from django.contrib import admin
from .models import Listing, Organization, Offer

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    pass
    

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    pass