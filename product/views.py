from django.shortcuts import render_to_response, get_object_or_404
from django.contrib import auth
from .models import Category, Product
from django.db.models.options import Options
import datetime


def categorylist(request):
    args = {}
    args['username'] = auth.get_user(request).username
    args['categorys'] = Category.objects.all()
    return render_to_response('categorylist.html', args)


def productslist(request, category_slug):
    args = {}
    category = Category.objects.get(slug=category_slug)
    args['products'] = Product.objects.filter(category=category.id)
    args['category_slug'] = category_slug
    return render_to_response('productslist.html', args)


def productditail(request, product_slug, category_slug):
    args = {}
    args['product'] = get_object_or_404(Product, slug=product_slug)
    return render_to_response('productditail.html', args)

def lastadded(request):
    user = auth.get_user(request).username
    args = {}
    if user:
        now = datetime.datetime.now()
        earlier = now - datetime.timedelta(hours=24)
        args['lastproducts'] = Product.objects.filter(created_at__gt=earlier)
        args['username'] = user
    else:
        args['masseg'] = 'Available only to registered users'

    return render_to_response('lastadded.html', args)

