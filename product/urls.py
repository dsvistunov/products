from django.conf.urls import url
from . import views


app_name = 'products'
urlpatterns = [

    url(r'^products/$', views.categorylist, name='categorylist'),
    url(r'^products/(?P<category_id>[0-9]+)/$', views.productslist, name='productslist'),
    url(r'^products/(?P<category_id>[0-9]+)/(?P<product_id>[0-9]+)/$', views.productditail, name='product'),
    url(r'^lastadded/', views.lastadded, name='lastadded'),

]