from django.test import TestCase
from account.models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfileTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="testuser", email="test@gmail.com", password="mytestpass1234")

    def setUp(self):
        self.user = User.objects.get(
            username="testuser", email="test@gmail.com")

    def test_create_profile(self):
        user_profile = Profile.objects.get(user=self.user)
        self.assertTrue(isinstance(user_profile, Profile))
        self.assertTrue(user_profile.__str__(), self.user.full_name)
