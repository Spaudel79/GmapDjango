from django.test import TestCase
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class MyTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('test@gmail.com',
                                             'Testman')

    def test_user(self):
        self.assertEqual(self.user.email, 'test@gmail.com')

    def tearDown(self):
        self.user.delete()


