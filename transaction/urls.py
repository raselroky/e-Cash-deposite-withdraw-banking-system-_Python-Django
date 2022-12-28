from transaction import views
from django.urls import path,include


urlpatterns = [
    path('transaction/',views.Transaction),
]