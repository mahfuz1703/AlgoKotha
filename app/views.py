from django.shortcuts import render
from .models import Jobs, Companies, companyRequest, UserFeedback
from django.contrib import messages
from django.shortcuts import redirect
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services.job_scraper import run_all_scrapers

# Create your views here.
@api_view(['POST', 'GET'])
def run_scraper(request):
    run_all_scrapers()
    return Response({"message": "Scraping started."})

def home(request):
    return render(request, 'home/index.html')

def signin(request):
    return render(request, 'auth/signin.html')

def jobs(request):
    jobs = Jobs.objects.all()
    companies = Companies.objects.all()

    # Searching functionality using multiple query using one field
    search_query = request.GET.get('randomQuery', '')

    # Job search by company name
    search_by_company = request.GET.get('company', '')
    if search_by_company:
        jobs = jobs.filter(company__name__icontains=search_by_company)


    if search_query:
        jobs = jobs.filter(
            job_title__icontains=search_query
        ) | jobs.filter(
            company__name__icontains=search_query
        ) | jobs.filter(
            job_location__icontains=search_query
        ) | jobs.filter(
            job_type__icontains=search_query
        ) | jobs.filter(
            job_salary__icontains=search_query
        )

    # Implement pagination if needed
    paginator = Paginator(jobs, 6)  # Show 6 jobs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs': page_obj,
        'companies': companies,
        'count': jobs.count(),
    }
    return render(request, 'home/jobs.html', context)

def job_detail(request, job_id):
    job = Jobs.objects.get(id=job_id)
    context = {
        'job': job,
    }
    return render(request, 'home/job_details.html', context)

def company_request(request):
    if request.method == 'POST':
        # Handle the company request form submission
        companyName = request.POST.get('companyName')
        website = request.POST.get('website')
        careerPage = request.POST.get('careerPage')
        # Save the request to the database
        new_request = companyRequest(companyName=companyName, website=website, careerPage=careerPage)
        new_request.save()
        messages.success(request, 'Company request submitted successfully! Thank you.')
        return redirect('company_request')
    return render(request, 'home/company_request.html')

def user_feedback(request):
    if request.method == 'POST':
        # Handle the user feedback form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')
        # Save the feedback to the database
        new_feedback = UserFeedback(name=name, email=email, feedback=feedback)
        new_feedback.save()
        messages.success(request, 'Thank you for your feedback! We appreciate your input.')
        return redirect('user_feedback')
    return render(request, 'home/user_feedback.html')
