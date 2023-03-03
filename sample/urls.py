"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from demo import views
from django.conf import settings
from django.contrib.auth import views as v
from django.views.static import serve 
from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
   
    path('home/',views.home),
    path('sent/',views.sent,name = "sent"),
    path('adminapp/',views.adminapp,name="adminapp"),
    path('feedback/',views.feedback,name="feedback"),
    path('delete/<int:id>', views.delete),
    path('sucess/',views.sucess,name = "sucess"),
    # path('repair/',views.repairs,name="repair"),
    path('book/',views.repairs,name="repair"),
    path('contact/',views.suggestions,name="contact"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

