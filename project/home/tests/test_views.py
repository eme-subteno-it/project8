""" Units tests for the home app """
from django.test import TestCase


class IndexViewTest(TestCase):

    def test_get_request(self):
        response = self.client.get('/')
        self.assertTemplateUsed('home/index.html')
        self.assertEqual(response.status_code, 200)

    def test_lang_fr(self):
        response = self.client.get('/', HTTP_ACCEPT_LANGUAGE='fr')
        self.assertContains(response, '<h1 class="text-uppercase text-white font-weight-bold">Du gras, oui, mais de qualité !</h1>', html=True)

    def test_lang_en(self):
        response = self.client.get('/', HTTP_ACCEPT_LANGUAGE='en')
        self.assertContains(response, '<h1 class="text-uppercase text-white font-weight-bold">Fat, yes, but of quality!</h1>', html=True)


class LegalNoticeViewTest(TestCase):

    def test_get_request(self):
        response = self.client.get('/legal-notices/')
        self.assertTemplateUsed('home/legal_notice.html')
        self.assertEqual(response.status_code, 200)
