from django.shortcuts import render
from .models import Jobs, Companies, companyRequest, UserFeedback
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def signin(request):
    return render(request, 'auth/signin.html')

def jobs(request):
    jobs = Jobs.objects.all()
    context = {
        'jobs': jobs,
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
