from django.urls import path,include
from . import views

app_name = '' # app이름 : 이름으로 접근
urlpatterns = [
    # view.py 연결 - 함수호출, app함수이름
    path('',views.index,name='index')
]
