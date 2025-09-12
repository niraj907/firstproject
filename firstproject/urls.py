from django.contrib import admin
from django.urls import path
from .views import *
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('admin/', admin.site.urls),
     path('about/', about, name='about'), 
     path('services/', services, name='services'), 
     path('login/', login_view, name='login'),
     path('register/', register_view, name='register'),
     path('logout/', logout_view, name='logout'), 
     path('contact/', contact, name='contact'), 
     path('saveenquiry/', saveEnquiry, name='saveenquiry'),
     path('calculator/', calculator, name='calculator'), 
     path('', include('news.urls')),
     path('submitForm/', submitForm, name='submitForm'), 
     path('marksheet/', marksheet), 
     path('', index, name='index'),
     path('test-email/', test_email, name='test_email'),
     path("__reload__/", include("django_browser_reload.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)