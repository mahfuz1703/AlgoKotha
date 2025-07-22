from django.contrib import admin
from .models import Companies, Jobs, companyRequest, UserFeedback

# Register your models here.
admin.site.register(Companies)
admin.site.register(Jobs)
admin.site.register(companyRequest)
admin.site.register(UserFeedback)
