from django.urls import path
from .views import blog, newDeatils

urlpatterns = [
    path('blog/', blog, name='blog'),
    path('blog/newDeatils/<slug:news_slug>/', newDeatils, name='newDeatils'),
]
