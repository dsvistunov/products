from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=10000)

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=10000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
