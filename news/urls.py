from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('national', views.national, name='national'),
    path('international', views.international, name='international'),
    path('newsdetail/<int:id>', views.newsdetail, name='newsdetail'),
    path('search/', views.search, name='search'),

]
