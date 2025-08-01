from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Companies(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    website = models.URLField(max_length=500, blank=True, null=True)
    careerPage = models.URLField(max_length=500, blank=True, null=True)
    logo = CloudinaryField('image', folder='Company_Logos', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Jobs(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    job_link = models.URLField(max_length=500, blank=False, null=False)
    job_apply_link = models.URLField(max_length=500, blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=False, null=False)
    job_vacancies = models.IntegerField(default=0)
    job_salary = models.CharField(max_length=255, blank=True, null=True)
    job_salary_type = models.CharField(max_length=50, blank=True, null=True)
    office_time = models.CharField(max_length=50, blank=True, null=True)
    job_type = models.CharField(max_length=50, blank=True, null=True)
    job_location = models.CharField(max_length=255, blank=True, null=True)
    job_deadline = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} at {self.company.name}"
    
class companyRequest(models.Model):
    companyName = models.CharField(max_length=255, blank=False, null=False)
    website = models.URLField(max_length=500, blank=True, null=True)
    careerPage = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"Request for {self.companyName}"
    
class UserFeedback(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False)
    feedback = models.TextField(blank=False, null=False)

    def __str__(self):
        return f"Feedback from {self.name}"
