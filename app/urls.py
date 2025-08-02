from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('jobs/', views.jobs, name='jobs'),
    path('jobs/details/<int:job_id>/', views.job_detail, name='job_details'),
    path('company-request/', views.company_request, name='company_request'),
    path('user-feedback/', views.user_feedback, name='user_feedback'),

    path("api/scrape-now/", views.run_scraper, name='run_scraper'),
]