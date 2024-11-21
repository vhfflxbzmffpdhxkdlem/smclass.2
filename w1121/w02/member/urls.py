from django.urls import path,include
from . import views

app_name='member'
urlpatterns = [
    path('logout/', views.login,name='logout'),
    path('login/', views.login,name='login'),
    path('event/', views.event,name='event'),
    path('membership1/', views.membership1,name='membership1'),
    path('membership2/', views.membership2,name='membership2'),
    path('membership3/', views.membership3,name='membership3'),
]
