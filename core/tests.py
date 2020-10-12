from django.test import TestCase
from django.urls import reverse


# Create your tests here.


class IndexPageTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
