from django.shortcuts import render

from service.models import Service
def services(request):
    servicesData = Service.objects.all().order_by('-service_title')[:3]
    print("Fetched services:", list(servicesData))
    return render(request, 'services.html', {'servicesData': servicesData})
