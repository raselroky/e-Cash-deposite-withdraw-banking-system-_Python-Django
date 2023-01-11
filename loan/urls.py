from django.urls import path,include
from . import views

urlpatterns = [
    path('loans/',views.LoanPossible.as_view())
]