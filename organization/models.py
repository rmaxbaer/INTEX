from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Organization(User):

    company_name = models.CharField(max_length=50)
    size = models.CharField(max_length=4, blank=True)
    sectors = models.CharField(max_length=4, blank=True)
    description = models.TextField(blank=True)
    date_founded = models.DateField(auto_now=False, auto_now_add=False, blank=True)

    def __str__(self):
        return self.company_name


class Listing(models.Model):

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50)
    job_description = models.TextField()
    contract_type = models.CharField(max_length=50, blank=True)
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
    status = models.CharField(max_length=50, default='extended')
    offer_accepted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

