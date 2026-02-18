from django.urls import path
from .views import job_detail, job_list


urlpatterns = [
    path('', job_list, name='job-list'),
    path('job-detail/<int:job_id>/', job_detail, name='job-detail'),
]
