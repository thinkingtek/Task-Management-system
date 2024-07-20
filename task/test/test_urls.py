from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from task.urls import *


# class TestUrls(SimpleTestCase):

#     def test_home_url_is_resolved(self):
#         url = reverse("task:index")
#         # print(resolve(url))
#         self.assertEqual(resolve(url).func, Index.as_view())
