from django.contrib import admin
from .models import Skill, Applicant, Application

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass
    

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    pass

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    pass
