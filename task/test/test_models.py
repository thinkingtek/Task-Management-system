from django.test import TestCase
from task.models import Task
from account.models import User


class TaskTest(TestCase):

    fixtures = [
        'tasks.json',
        'users.json'
    ]

    def setUp(self):
        self.user = User.objects.get(
            username="louisepabor", email="paborlouise@gmail.com")
        self.assigned_to = User.objects.get(
            username="james24", email="james24@gmail.com")

    def test_task(self):
        task = Task.objects.get(pk=2)
        self.assertTrue(task.__str__(), task.title)
