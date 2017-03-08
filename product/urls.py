from django.conf.urls import url
from . import views


app_name = 'products'
urlpatterns = [

    url(r'^products/$', views.categorylist, name='categorylist'),
    url(r'^products/(?P<category_slug>[\w-]+)/$', views.productslist, name='productslist'),
    url(r'^products/(?P<category_slug>[\w-]+)/(?P<product_slug>[\w-]+)/$', views.productditail, name='product'),
    url(r'^lastadded/', views.lastadded, name='lastadded'),

]