from django.shortcuts import render


# Create your views here.
# 商品首页界面
def IndexView(request):
    return render(request, 'index.html')
