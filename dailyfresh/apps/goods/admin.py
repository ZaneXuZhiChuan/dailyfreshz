from django.contrib import admin
from django.core.cache import cache
from celery_tasks.tasks import generate_static_index_html

from apps.goods.models import GoodsType, IndexPromotionBanner, IndexGoodsBanner, IndexTypeGoodsBanner


class BaseModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        #  保留父类的保存功能
        super().save_model(request, obj, form, change)
        #  发出任务，重新生成 static/index.html 页面
        generate_static_index_html.delay()
        #  后台对页面进行数据修改时候需要清楚页面之前的的缓存
        cache.delete('index_page_data')

    def delete_model(self, request, obj):
        #  保留父类的删除功能
        super().delete_model(request, obj)
        #  发出任务，重新生成 static/index.html 页面
        generate_static_index_html.delay()
        #  后台对页面进行数据修改时候需要清楚页面之前的的缓存
        cache.delete('index_page_data')


# 自定义模型管理类继承BaseModelAdmin功能
class GoodsTypeAdmin(BaseModelAdmin):
    pass


class IndexGoodsBannerAdmin(BaseModelAdmin):
    pass


class IndexTypeGoodsBannerAdmin(BaseModelAdmin):
    pass


class IndexPromotionBannerAdmin(BaseModelAdmin):
    pass


admin.site.register(GoodsType, GoodsTypeAdmin)
admin.site.register(IndexGoodsBanner, IndexGoodsBannerAdmin)
admin.site.register(IndexTypeGoodsBanner, IndexTypeGoodsBannerAdmin)
admin.site.register(IndexPromotionBanner, IndexPromotionBannerAdmin)

