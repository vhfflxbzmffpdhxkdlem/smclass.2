from django.urls import path,include
from . import views
# . 은 현재폴더

app_name='students'
urlpatterns = [
    path('write/', views.write,name='write'),
]
