from django.urls import path,include
from . import views
# . 은 현재폴더

app_name=''
urlpatterns = [
    path('', views.index,name='index'),
]
