from django.conf.urls import url
from .views import IndexView, CategoryListView, ProductListView, ProductDetailView, LastAdded


app_name = 'products'
urlpatterns = [
    url(r'^products/(?P<category_slug>[\w-]+)/(?P<slug>[\w-]+)/$', ProductDetailView.as_view(), name='product'),
    url(r'^products/(?P<slug>[\w-]+)/$', ProductListView.as_view(), name='productslist'),
    url(r'^products/$', CategoryListView.as_view(), name='categories'),
    url(r'^lastadded/', LastAdded.as_view(), name='lastadded'),
    url(r'^$', IndexView.as_view(), name='indexview'),
]
