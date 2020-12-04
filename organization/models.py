from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Organization(User):

    company_name = models.CharField(max_length=50)
    size = models.CharField(max_length=4)
    sectors = models.CharField(max_length=4)
    description = models.TextField()
    date_founded = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name


class Listing(models.Model):

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50)
    job_description = models.TextField()
    contract_type = models.CharField(max_length=50)
    compensation = models.CharField(max_length=50)
    relocation_assistance = models.BooleanField(default=False)
    skills = models.ManyToManyField('applicant.Skill')

    def __str__(self):
        return self.name


class Position(models.Model):

    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Offer(models.Model):

    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    applicant = models.ForeignKey('applicant.Applicant', on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    deadline = models.DateTimeField(auto_now=False, auto_now_add=False)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name

