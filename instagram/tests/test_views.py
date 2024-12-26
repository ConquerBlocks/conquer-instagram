from django.test import TestCase
from django.urls import reverse


class TestCoreView(TestCase):

  def test_home_view(self):
    url = reverse('home')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
