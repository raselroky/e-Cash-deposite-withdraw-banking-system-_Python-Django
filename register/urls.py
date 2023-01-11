
from register import views
from django.urls import path,include


urlpatterns = [
    path('register/',views.RegisterAPI.as_view()),
    path('login/',views.LoginAPI.as_view()),

]