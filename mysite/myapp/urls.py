"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index),
    path('priceasc/', views.priceOrderAsc),
    path('pricedesc/', views.priceOrderDesc),
    path('sqft/', views.sqftOrder),
    path('bed/', views.bedOrder),
    path('bath/', views.bathOrder),
    path('apartments/', views.aptOrder),
    path('houses/', views.houseOrder),
    path('chat/', views.chatindex),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('login/', auth_views.LoginView.as_view()),
    path('register/', views.register),
    path('logout/', views.logout_view),
    path('addproperty/', views.addproperty),
    path('apply/<int:prop_id>/', views.applyproperty),
]
