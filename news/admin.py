from django.contrib import admin
from django.utils.html import format_html
from .models import News



class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'display_news_description', 'news_image_preview', 'published_date')


    def display_news_description(self, obj):
        return format_html(obj.news_decs)
    display_news_description.short_description = 'NEWS DECS'

    def news_image_preview(self, obj):
        if obj.news_image:
            return format_html('<img src="{}" width="60" height="40" />', obj.news_image.url)
        return "-"
    news_image_preview.short_description = 'Image Preview'

admin.site.register(News, NewsAdmin)