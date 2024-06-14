from django.shortcuts import render, get_object_or_404

from applications.news.models import News


def news_list_view(request):
    all_news = News.objects.all()
    tech_news = all_news.filter(news_type='tech')
    media_news = all_news.filter(news_type='media')
    context = {
        'all_news': all_news,
        'tech_news': tech_news,
        'media_news': media_news,
    }
    return render(request, 'news/news_list.html', context)


def news_details_view(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'news/news_details.html', context={'news': news})
