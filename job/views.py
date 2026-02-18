from django.shortcuts import render

from job.models import Job

# Create your views here.

def job_list(request):
    context = {}
    return render(request, 'job/job-list.html', context)

def job_detail(request, job_id):
    job_detail = Job.objects.get(id=job_id)
    context = {
        'job_detail': job_detail
    }
    
    return render(request, 'job/job-detail.html', context)




