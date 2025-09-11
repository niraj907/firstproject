from django.db import models

# Create your models here.


class contactEnquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=65)
    websiteLink = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)