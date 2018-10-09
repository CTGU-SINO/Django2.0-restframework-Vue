"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from MxShop.settings import MEDIA_ROOT
from rest_framework.documentation import include_docs_urls
# from goods.views_base import GoodsListView
from goods.views import GoodsListView, GoodsListView1, GoodsListViewSet, GoodsListViewSet1
import xadmin

goods_list = GoodsListViewSet1.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('goods', GoodsListView.as_view(), name='goods-list'),
    path('goods1', GoodsListView1.as_view(), name='goods-list'),
    path('goodsSet', GoodsListViewSet.as_view(), name='goods-list'),
    path('goodsSet1', goods_list, name='goods-list'),
    re_path('^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    path('docs/', include_docs_urls(title='慕学生鲜'))
]
