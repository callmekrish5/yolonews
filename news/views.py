from django.shortcuts import render

from news_user.auth import user_only
from .models import *
from django.db.models import Q
from django.contrib import messages
from .filters import NewsFilter


# Create your views here.
@user_only
def home(request):
    national_news = News.objects.filter(category=1).order_by("-id")[:10]
    international_news = News.objects.filter(category=2).order_by("-id")[:10]
    breaking_news = News.objects.filter(recent=True).order_by("-id")[:3]

    context = {
        "national_news": national_news,
        "international_news": international_news,
        "breaking_news": breaking_news,
    }

    return render(request, "news/home.html", context)


def national(request):
    news = News.objects.filter(category=1).order_by("-id")
    news_filter = NewsFilter(request.GET, queryset=news)
    news_final = news_filter.qs

    return render(
        request, "news/national.html", {"news": news_final, "news_filter": news_filter}
    )


def international(request):
    news = News.objects.filter(category=2).order_by("-id")
    news_filter = NewsFilter(request.GET, queryset=news)
    news_final = news_filter.qs

    return render(
        request,
        "news/international.html",
        {"news": news_final, "news_filter": news_filter},
    )


def newsdetail(request, id):
    news = News.objects.get(id=id)
    return render(request, "news/newsdetail.html", {"news": news})


def search(request):
    if request.method == "GET":
        query = request.GET["query"]

        if len(query) > 20:
            messages.warning(request, "Query is too long")
            news = News.objects.none()

        elif len(query) == 0 or len(query) < 2:
            news = News.objects.none()
            messages.error(request, "Type something")

        news = News.objects.filter(
            Q(date__icontains=query)
            | Q(heading__icontains=query)
            | Q(details__icontains=query)
        )
        context = {"news": news, "query": query}
        return render(request, "news/search.html", context)
