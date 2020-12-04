from django.test import TestCase
from user.models import User


class UserModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test_username',
            first_name='test_first_name',
            last_name='test_last_name',
            email='email@test.com',
            password='test_password_61',
            subscribed=True
        )

    def test_email_max_length(self):
        user = User.objects.get(id=self.user.id)
        max_length = user._meta.get_field('email').max_length
        self.assertEquals(max_length, 100)
