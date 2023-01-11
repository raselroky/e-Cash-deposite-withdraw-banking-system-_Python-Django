from transaction import views
from django.urls import path,include


urlpatterns = [
    path('transaction/',views.Transaction.as_view()),
    path('mypresentData/',views.MyPresentData.as_view()),
    path('transfer/',views.Transfer.as_view()),
]