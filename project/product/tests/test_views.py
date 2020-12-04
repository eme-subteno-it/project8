from django.test import TestCase, override_settings
from user.models import User
from product.models import Product
from product.views import SearchProduct


class SearchProductViewTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name='Nutella',
            description='description',
            store='Auchan',
            nutriscore='2',
            nutriscore_grade='B',
            image='https://static.openfoodfacts.org/images/products/322/885/700/0852/front_fr.134.400.jpg',
            url_api='https://fr.openfoodfacts.org/produit/3502110009449/pur-jus-d-orange-sans-pulpe-tropicana',
            fat_level='low',
            satured_fat_level='low',
            sugars_level='moderate',
            salt_level='low',
            fat_g=0,
            satured_fat_g=0,
            sugars_g=8.9,
            salt_g=0
        )
        self.query = 'nutella'

    def test_get_request(self):
        response = self.client.get('/search/?search=%s' % self.query)
        self.assertEqual(response.context['products'][0], self.product)
        self.assertTemplateUsed(response, 'product/result.html')
        self.assertEqual(response.status_code, 200)

    @override_settings(LANGUAGE_CODE='en-US', LANGUAGES=(('en', 'English'),))
    def test_get_request_no_query(self):
        response = self.client.get('/search/')
        message = 'This product does not exist.'
        self.assertEqual(response.context['error'], message)
        self.assertTemplateUsed(response, 'product/result.html')
        self.assertEqual(response.status_code, 200)


class SubstitutesViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test_username',
            first_name='test_first_name',
            last_name='test_last_name',
            email='email@test.com',
            password='test_password_61',
            subscribed=True
        )
        self.product = Product.objects.create(
            name='Nutella',
            description='description',
            store='Auchan',
            nutriscore='2',
            nutriscore_grade='B',
            image='https://static.openfoodfacts.org/images/products/322/885/700/0852/front_fr.134.400.jpg',
            url_api='https://fr.openfoodfacts.org/produit/3502110009449/pur-jus-d-orange-sans-pulpe-tropicana',
            fat_level='low',
            satured_fat_level='low',
            sugars_level='moderate',
            salt_level='low',
            fat_g=0,
            satured_fat_g=0,
            sugars_g=8.9,
            salt_g=0
        )

    def test_get_request(self):
        response = self.client.get('/search/substitutes/%s/' % self.product.id)
        self.assertTemplateUsed(response, 'product/substitutes.html')
        self.assertEqual(response.status_code, 200)

    def test_post_request_without_user(self):
        response = self.client.post('/save_substitute/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'status': 'error'}
        )

    def test_post_request_with_user(self):
        self.client.login(username='test_username', password='test_password_61')
        response = self.client.post('/save_substitute/', {'product_id': self.product.id})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'status': 'success'}
        )
        self.client.logout()


class ProductViewTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name='Nutella',
            description='description',
            store='Auchan',
            nutriscore='2',
            nutriscore_grade='B',
            image='https://static.openfoodfacts.org/images/products/322/885/700/0852/front_fr.134.400.jpg',
            url_api='https://fr.openfoodfacts.org/produit/3502110009449/pur-jus-d-orange-sans-pulpe-tropicana',
            fat_level='low',
            satured_fat_level='low',
            sugars_level='moderate',
            salt_level='low',
            fat_g=0,
            satured_fat_g=0,
            sugars_g=8.9,
            salt_g=0
        )

    def test_get_request(self):
        response = self.client.get('/product-%s/' % self.product.id)
        self.assertTemplateUsed(response, 'product/product.html')
        self.assertEqual(response.status_code, 200)

    def test_get_request_no_product(self):
        response = self.client.get('/product-35/')
        self.assertTemplateUsed(response, '404.html')
        self.assertEqual(response.status_code, 404)
