from django.conf.urls import url
from . import views

app_name = 'products'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^product_list/', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
