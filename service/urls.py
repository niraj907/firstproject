from django.urls import path

from service.views import services


urlpatterns = [
    path('services/', services, name='services'),
]
