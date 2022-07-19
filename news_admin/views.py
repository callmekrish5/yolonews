from django.shortcuts import render, redirect
from news.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import NewsForm



# Create your views here.


def admin_dashboard(request):
    subscribers=User.objects.filter(is_staff=0).count()
    reporters= Reporter.objects.all().count()
    admins= User.objects.filter(is_staff=1).count()
    news= News.objects.all().count()
    nationalnews= News.objects.filter(category=1).count()
    internationalnews= News.objects.filter(category=2).count()
    recentnews= News.objects.all().order_by('-id')[:10]


    context={
        'subscribers':subscribers,
        'reporters':reporters,
        'admins':admins,
        'news':news,
        'nationalnews':nationalnews,
        'internationalnews':internationalnews,
        'recentnews':recentnews


    }
    return render(request, 'news_admin/dashboard.html',context)

def addnews(request):
    if request.method == 'GET':
        form=NewsForm
        context={'form':form}
        return render(request, "news_admin/addnews.html", context)

    else:
        form = NewsForm(request.POST, request.FILES)
      
        if form.is_valid():
            form.save()
            print(form)
            messages.success(request, 'News added successfully!')
            return redirect('news_admin:dashboard')
        else:
            form=NewsForm
            context={'form':form}
            messages.error(request, 'Error in saving data!!')

            return render(request, "news_admin/addnews.html", context)
  
    
