from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.admin_dashboard, name='dashboard'),
    path('addnews', views.addnews, name='addnews'),

    # path('', views.userlogin, name='login'),
    # path('logout', views.userlogout, name='logout')


]
