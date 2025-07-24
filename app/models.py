from django.db import models

# Create your models here.
class Companies(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    website = models.URLField(max_length=500, blank=True, null=True)
    careerPage = models.URLField(max_length=500, blank=True, null=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    

    def __str__(self):
        return self.name
    
class Jobs(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    location = models.CharField(max_length=255, blank=True, null=True)
    employmentType = models.CharField(max_length=50, choices=[
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
    ], default='full_time', blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    applyLink = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.title} at {self.company.name}"
    
    def get_FIELD_display(self):
        return self.get_employmentType_display() if self.employmentType else 'Not specified'
    
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
