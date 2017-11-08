from django.conf.urls import url, include
from django.contrib import admin
from customer import views
from django.views.static import serve
from .settings import MEDIA_ROOT




urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^', include('products.urls', namespace='products')),


]
