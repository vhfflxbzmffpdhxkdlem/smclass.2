from django.urls import path,include
from . import views

app_name = ""
urlpatterns = [
    path('', views.landing,name="landing"),
    path('index/', views.main,name="main"),
]
