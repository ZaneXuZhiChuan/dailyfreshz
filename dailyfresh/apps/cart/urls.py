from django.conf.urls import url
from apps.cart.views import CartAddView

urlpatterns = [
    url(r'^add$', CartAddView.as_view(), name='logout'), # 购物车记录添加
]
