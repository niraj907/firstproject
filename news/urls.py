from django.urls import path
from news.views import blog, newDeatils


urlpatterns = [
    path('blog/', blog, name='blog'),
    path('blog/newDeatils/<slug:news_slug>/', newDeatils, name='newDeatils'),
]
