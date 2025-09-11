from django.shortcuts import render
from news.models import News
from django.core.paginator import Paginator
from django.shortcuts import render,  get_object_or_404

def blog(request):
    st = request.GET.get('newsname')  # Search term
    if st:
        newsData = News.objects.filter(news_title__icontains=st).order_by('-id')
    else:
        newsData = News.objects.all().order_by('-id')

    paginator = Paginator(newsData, 3)  # 3 news per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'newsname': st or "",  # send search term to template
    }
    return render(request, 'blog.html', context)


def newDeatils(request, news_slug):
    newsData = get_object_or_404(News, news_slug=news_slug)
    return render(request, 'newDeatils.html', {'newsData': newsData})