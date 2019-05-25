# from django.conf.urls import url
# from apps.goods import views
#
# urlpatterns = [
#     url(r'^$', views.IndexView, name='index'), # 首页
# ]
from django.urls import path
from apps.goods import views

urlpatterns = [
    path('index', views.IndexView, name='index'),  # 首页
]
