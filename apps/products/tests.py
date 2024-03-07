from django.test import TestCase
from django.urls import reverse


class ProductSearchAPITest(TestCase):
    def test_search_products(self):
        response = self.client.get(reverse('product-search'), {'search': 'elektronika'})
        self.assertEqual(response.status_code, 200)
