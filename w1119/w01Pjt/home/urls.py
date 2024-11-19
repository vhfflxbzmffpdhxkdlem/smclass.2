from django.urls import path,include  # include 추가
from . import views

app_name='' # app_name 설정
urlpatterns = [
        # url링크 ,views함수호출 ,name링크
    path('', views.index,name='index'),
]
