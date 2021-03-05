""" All tests for the product views application """
from django.test import TestCase, override_settings
from user.models import User
from product.models import Product, Category


class SearchProductViewTest(TestCase):
    """
        Testing the search product view.
        This class create a product in database test
        and a search to test the result.
    """

    def setUp(self):
        self.product = Product.objects.create(
            name='Nutella',
            description='description',
            store='Auchan',
            nutriscore='2',
            nutriscore_grade='b',
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
    """
        Testing the substitutes view.
        This class create a product in database test
        and a user to test the result and saving substitutes.
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_username',
            first_name='test_first_name',
            last_name='test_last_name',
            email='email@test.com',
            password='test_password_61',
            subscribed=True
        )
        self.category = Category.objects.create(
            name='Boisson',
        )
        self.product = Product.objects.create(
            name='Nutella',
            description='description',
            store='Auchan',
            nutriscore='2',
            nutriscore_grade='d',
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
        self.product.category_ids.add(self.category)
        self.substitute = Product.objects.create(
            name='Confiture',
            description='description',
            store='Auchan',
            nutriscore='1',
            nutriscore_grade='c',
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

        self.substitute2 = Product.objects.create(
            name='Pain de mie',
            description='description',
            store='Auchan',
            nutriscore='1',
            nutriscore_grade='a',
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

        self.substitute3 = Product.objects.create(
            name='Confiture',
            description='description',
            store='Auchan',
            nutriscore='1',
            nutriscore_grade='b',
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

        self.substitute.category_ids.add(self.category)
        self.substitute2.category_ids.add(self.category)
        self.substitute3.category_ids.add(self.category)

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
        self.client.login(username='email@test.com', password='test_password_61')
        response = self.client.post('/save_substitute/', {'product_id': self.product.id})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'status': 'success'}
        )
        self.client.logout()

    def test_display_list_substitutes(self):
        response = self.client.get('/search/substitutes/%s/' % self.product.id)
        substitutes = response.context['substitutes']
        nutriscores = []
        for sub in substitutes:
            nutriscores.append(sub.nutriscore_grade)

        self.assertEqual(nutriscores, sorted(nutriscores))


class ProductViewTest(TestCase):
    """
        Testing the product view.
        This class create a product in database test
        to test if the user display the product page.
    """
    def setUp(self):
        self.product = Product.objects.create(
            name='Nutella',
            description='description',
            store='Auchan',
            nutriscore='2',
            nutriscore_grade='b',
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
