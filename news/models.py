from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class News(models.Model):
    news_title = models.CharField(max_length=255)
    news_image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    news_decs = HTMLField()
    published_date = models.DateTimeField(auto_now_add=True)
    news_slug = AutoSlugField(populate_from='news_title', unique=True, null=True, default=None)
    # news_slug = AutoSlugField(populate_from='news_title', unique=True)

    def __str__(self):
        return self.news_title