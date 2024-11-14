from django.urls import path,include
from . import views
# . 은 현재폴더

app_name='event'
urlpatterns = [
    path('eventView/', views.eventView,name='eventView'),
]
