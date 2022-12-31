
from django.contrib import admin
from django.urls import path,include
from contacts import views

urlpatterns = [
    path('contacts/',views.Contact_Us)
]
