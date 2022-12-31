
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('register.urls')),
    path('api/',include('transaction.urls')),
    path('api/',include('contacts.urls')),

]
