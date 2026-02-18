from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from jobportal.views import home, about, contact, error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/', include('job.urls')),
    path('account/', include('account.urls')),
    path('', home, name='home'),
    path('404/', error, name='404'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)