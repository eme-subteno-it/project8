from django.test import TestCase


class IndexViewTest(TestCase):

    def test_get_request(self):
        response = self.client.get('/')
        self.assertTemplateUsed('home/index.html')
        self.assertEqual(response.status_code, 200)


class LegalNoticeViewTest(TestCase):

    def test_get_request(self):
        response = self.client.get('/legal-notices/')
        self.assertTemplateUsed('home/legal_notice.html')
        self.assertEqual(response.status_code, 200)
