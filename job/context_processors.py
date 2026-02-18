from .models import Category, Job

def all_categories(request):
    return {
        'categories': Category.objects.all()
    }
def all_jobs(request):
    return {
        'jobs': Job.objects.all()
    }