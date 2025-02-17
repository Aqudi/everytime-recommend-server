"""project_everyReco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.home, name="home"),
    path('temp/', main.views.temp, name="temp"),
    path('result/', main.views.result, name="result"),
    path('result/search/', main.views.search, name="search"),
    path('show/', main.views.show, name="show"),
    path('like/<int:lecture_id>', main.views.like, name="like"),
    path('mypage/', main.views.mypage, name="mypage"),
    path('accounts/', include('allauth.urls')),

    path('total-search/', main.views.total_search, name="total_search"),
]
