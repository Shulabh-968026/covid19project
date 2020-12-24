from django.contrib import admin
from covidapp import views
from django.urls import path

urlpatterns = [
    path('',views.helloworld),
]