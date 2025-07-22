from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def signin(request):
    return render(request, 'auth/signin.html')

def jobs(request):
    return render(request, 'home/jobs.html')

def job_detail(request):
    # Placeholder for job detail view
    return render(request, 'home/job_details.html')

def company_request(request):
    return render(request, 'home/company_request.html')

def user_feedback(request):
    return render(request, 'home/user_feedback.html')
