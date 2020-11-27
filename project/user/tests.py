from django.test import TestCase
from .models import User


class RegisterViewTest(TestCase):

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
        self.failUnlessEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/my_account.html')
        self.client.logout()


class MySubstitutesViewTest(TestCase):

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
        response = self.client.get('/my/substitutes/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/my/substitutes/')
