import datetime
from django.test import TestCase
from django.urls import reverse
from .models import Category, Product


def create_product(hours):
    category = Category.objects.create(name='category1')
    created = datetime.datetime.now() - datetime.timedelta(hours=hours)
    return Product.objects.create(created_at=created, category=category, price=0)

class TestCalls(TestCase):

    def test_call_lastadded(self):
        response = self.client.get(reverse('products:lastadded'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lastadded.html')
        self.assertContains(response, "Available only to registered users")

    def test_call_lastadded_login_user(self):
        self.client.login(username='user', password='test')
        response = self.client.get(reverse('products:lastadded'))
        product = create_product(24)
        self.assertContains(response, product)
