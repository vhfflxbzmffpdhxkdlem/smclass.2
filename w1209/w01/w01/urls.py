from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('loginpage/', include('loginpage.urls')),
    path('', include('home.urls')),
]
