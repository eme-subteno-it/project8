""" All tests for the user views application """
from django.test import TestCase
from django.db.models.query import QuerySet
from user.models import User
from product.models import Product


class RegisterViewTest(TestCase):
    """ Class to test the view register account """

    def setUp(self):
        self.form_class = {
            'username': 'test_form',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'email': 'email@test.com',
            'password1': 'test_password_1',
            'password2': 'test_password_1',
            'subscribed': True,
        }

    def test_get_request(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_post_request(self):
        response = self.client.post('/register/', self.form_class)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/my/account/')

    def test_post_request_if_wrong_form(self):
        form = self.form_class
        form['password2'] = 'wrong_password'
        response = self.client.post('/register/', form)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.wsgi_request.path, '/register/')


class LoginViewTest(TestCase):
    """ Class to test the view login account """

    def setUp(self):
        User.objects.create_user(
            username='test_username',
            first_name='test_first_name',
            last_name='test_last_name',
            email='email@test.com',
            password='test_password_61',
            subscribed=True
        )
        self.form_class = {
            'username': 'test_username',
            'password': 'test_password_61',
        }

    def test_get_request(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_post_request(self):
        response = self.client.post('/login/', self.form_class)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/my/account/')

    def test_post_request_if_wrong_form(self):
        form = self.form_class
        form['password'] = 'wrong_password'
        response = self.client.post('/login/', form)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.wsgi_request.path, '/login/')


class MyAccountViewTest(TestCase):
    """ Class to test the view my account """

    def setUp(self):

        User.objects.create_user(
            username='test_username',
            first_name='test_first_name',
            last_name='test_last_name',
            email='email@test.com',
            password='test_password_61',
            subscribed=True
        )

    def test_get_request(self):
        response = self.client.get('/my/account/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/my/account/')

    def test_user_connected(self):
        self.client.login(username='test_username', password='test_password_61')
        response = self.client.get('/my/account/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/my_account.html')
        self.client.logout()


class MySubstitutesViewTest(TestCase):
    """ Class to test the view my substitutes """

    def setUp(self):
        self.user = User.objects.create_user(
            username='test_username',
            first_name='test_first_name',
            last_name='test_last_name',
            email='email@test.com',
            password='test_password_61',
            subscribed=True
        )
        self.product = Product.create_product(
            name='Jus d\'orange',
            description='description',
            store='Auchan',
            nutriscore='1',
            nutriscore_grade='c',
            image='https://static.openfoodfacts.org/images/products/322/885/700/0852/front_fr.134.400.jpg',
            url_api='https://fr.openfoodfacts.org/produit/3502110009449/pur-jus-d-orange-sans-pulpe-tropicana',
            category_ids=[1],
            fat_level='low',
            satured_fat_level='low',
            sugars_level='moderate',
            salt_level='low',
            fat_g=0,
            satured_fat_g=0,
            sugars_g=8.9,
            salt_g=0
        )
        self.product.user_ids.add(self.user)

    def test_get_request(self):
        response = self.client.get('/my/substitutes/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/my/substitutes/')

    def test_get_user_connected(self):
        self.client.login(username='test_username', password='test_password_61')
        response = self.client.get('/my/substitutes/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/my_substitutes.html')

        self.assertEqual(response.context['products'][0], self.product)
        self.assertEqual(type(response.context['products']), QuerySet)
        self.assertEqual(len(response.context['products']), 1)
        self.assertEqual(type(response.context['len']), int)
        self.client.logout()

    def test_post_request(self):
        response = self.client.post('/my/substitutes/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/my/substitutes/')

    def test_post_user_connected(self):
        self.client.login(username='test_username', password='test_password_61')
        response = self.client.get('/my/substitutes/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/my_substitutes.html')

        self.assertEqual(response.context['products'][0], self.product)
        self.assertEqual(type(response.context['products']), QuerySet)
        self.assertEqual(len(response.context['products']), 1)
        self.assertEqual(type(response.context['len']), int)
        self.client.logout()


class LogoutAccountViewTest(TestCase):
    """ Class to test the logout account """

    def setUp(self):
        User.objects.create_user(
            username='test_username',
            first_name='test_first_name',
            last_name='test_last_name',
            email='email@test.com',
            password='test_password_61',
            subscribed=True
        )

    def test_get_request_user_connected(self):
        self.client.login(username='test_username', password='test_password_61')
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
        self.client.logout()

    def test_get_request_user_no_connected(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
