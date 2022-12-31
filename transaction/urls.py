from transaction import views
from django.urls import path,include


urlpatterns = [
    path('transaction/',views.Transaction),
    path('mypresentData/',views.MyPresentData),
    path('transfer/',views.Transfer),
]