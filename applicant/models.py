from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Skill(models.Model):

    skill_name = models.CharField(max_length=50)
    proficiency = models.IntegerField()

    def __str__(self):
        return self.skill_name

class Applicant(User):

    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    resume = models.FileField(upload_to=None, max_length=100, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Application(models.Model):

    application_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    listing = models.ForeignKey('organization.Listing', on_delete=models.CASCADE)
    offer_made = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
