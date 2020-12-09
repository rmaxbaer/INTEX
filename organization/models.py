from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Organization(User):

    company_name = models.CharField(max_length=50)
    size = models.CharField(max_length=4, blank=True)
    sectors = models.CharField(max_length=4, blank=True)
    description = models.TextField(blank=True)
    date_founded = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zip = models.CharField(max_length=50, blank=True)
    profile_picture = models.ImageField(upload_to='profile_picture/', height_field=None, width_field=None, max_length=None, blank=True)
    cover_picture = models.ImageField(upload_to='cover_picture/', height_field=None, width_field=None, max_length=None, default='cover_picture/cover-pattern.jpg')

    def __str__(self):
        return self.company_name


class Listing(models.Model):

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50)
    job_description = models.TextField()
    contract_type = models.CharField(max_length=50, blank=True, default="--")
    compensation = models.CharField(max_length=50)
    relocation_assistance = models.BooleanField(default=False)
    skills = models.ManyToManyField('applicant.Skill', blank=True)
    positions_available = models.IntegerField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.job_title


class Offer(models.Model):

    application = models.ForeignKey('applicant.Application', on_delete=models.CASCADE)
    deadline = models.DateTimeField(auto_now=False, auto_now_add=False)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    message = models.TextField(blank=True)
    compensation = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=50, default='extended')
    offer_accepted = models.BooleanField(default=False)
