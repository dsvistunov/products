from django.shortcuts import get_object_or_404
from .models import Category, Product
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404
from django.views.generic import ListView, DetailView
import datetime


class IndexView(ListView):
    context_object_name = 'home_list'
    template_name = 'itemslist.html'
    queryset = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class CategoryListView(ListView):
    model = Category
    template_name = 'categorylist.html'


class ProductListView(ListView):
    model = Product
    template_name = 'productslist.html'

    def get_queryset(self, *args, **kwargs):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        if not category:
            raise Http404
        return Product.objects.filter(category=category.id)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'productditail.html'

    def get_object(self, *args, **kwargs):
        category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        if not category:
            raise Http404
        return Product.objects.get(slug=self.kwargs['slug'])


@method_decorator(login_required, name='dispatch')
class LastAdded(ListView):
    model = Product
    queryset = Product.objects.filter(created_at__gt=datetime.datetime.now() - datetime.timedelta(hours=24))
    template_name = 'lastadded.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LastAdded, self).dispatch(*args, **kwargs)
