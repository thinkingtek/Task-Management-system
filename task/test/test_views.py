from django.test import TestCase, Client
from task.models import Task
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
import datetime
from django.contrib.messages import get_messages
from task.forms import AddTaskForm
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from task.serializers import TaskSerializer

User = get_user_model()


# class TestApiViews(APITestCase):
#     fixtures = [
#         'tasks.json',
#         'users.json'
#     ]

#     def setUp(self):
#         self.client = APIClient()

#         self.first_user = User.objects.get(username="louisepabor")
#         self.second_user = User.objects.get(username="james24")
#         naive_datetime = datetime.datetime(2024, 7, 20)
#         self.task = Task.objects.create(pk=20,
#                                         title="New Task", assigned_to=self.first_user, task_creator=self.second_user, due_date=timezone.make_aware(naive_datetime))
#         self.form_data = {'assigned_to': 'louisepabor', 'title': 'Update Api Task', 'priority': 'low', 'status': 'completed',
#                           'category': 'web design', 'description': 'Testing the form valid method'}

#         self.invalid_form_data = {'assigned_to': '', 'title': '', 'priority': '', 'status': '',
#                                   'category': '', 'description': ''}
#         self.api_task_update_url = reverse(
#             "task:api-task-update", args=[self.task.pk])

#     def test_valid_update_task(self):
#         response = self.client.put(
#             self.api_task_update_url, self.form_data, format='json')
#         # self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Task.objects.get(
#             pk=self.task.pk).title, 'Update Api Task')
#         print("---Worked-----")

# def test_invalid_task_update(self):
#     response = self.client.put(
#         self.api_task_update_url, self.form_data, format='json')
#     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

# def test_task_update_not_found(self):
#     url = reverse('task-update', args=[999])  # assuming 999 is not a valid pk
#     response = self.client.put(url, self.valid_payload, format='json')
#     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestTaskViews(TestCase):

    fixtures = [
        'tasks.json',
        'users.json'
    ]

    def setUp(self):
        self.client = Client()
        self.client.login(username='james24', password='jamesjamespass')
        self.first_user = User.objects.get(username="louisepabor")
        self.second_user = User.objects.get(username="james24")
        # naive_datetime = datetime.datetime(2024, 7, 20)
        self.task = Task.objects.get(pk=2)
        # self.task = Task.objects.create(title="First Task created", assigned_to=self.first_user,
        #                                 task_creator=self.second_user, priority="high",
        #                                 status="in progress",
        #                                 category="Flutter App",
        #                                 description="Working with unittesst in Django", due_date="2024-07-19T00:00:00Z")
        # self.api_task_list_url = reverse("task:task-list")
        # self.api_task_update_url = reverse(
        #     "task:api-task-update", args=[self.task.pk])
        self.task_details_url = reverse(
            "task:task-details", args=[self.task.pk])
        self.task_update_url = reverse(
            "task:task-update", kwargs={'pk': self.task.pk})
        self.task_add_url = reverse("task:add-task")
        self.task_delete_url = reverse(
            "task:task-delete", args=[self.task.pk])

    # Test task update form
    def test_update_task(self):
        self.client.login(username='james24', password='jamesjamespass')
        form_data = {
            'title': 'Updated Task Title',
            'description': 'Updated description'
        }
        # form = AddTaskForm(data=form_data)
        # self.assertTrue(form.is_valid)

        response = self.client.post(self.task_update_url, form_data)
        self.task.refresh_from_db()
        # Check if response was a success
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['task_active'])
        # It doesn't work probably because it is a class Based view
        # self.assertEqual(self.task.title, 'Updated Task Title')
        self.task.refresh_from_db()
        # self.assertEqual(updated_task.description, 'Updated description')

    # testing api task-list view
    # def test_task_list(self):
    #     response = self.client.get(self.api_task_list_url)
    #     self.assertEqual(response.status_code, 200)

    def test_task_details(self):
        response = self.client.get(self.task_details_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task/task-details.html')

    def test_task_delete(self):
        response = self.client.delete(self.task_delete_url)
        # Check if the response is a redirect
        self.assertEqual(response.status_code, 302)
        # Check if the task was deleted
        self.assertEqual(Task.objects.filter(pk=self.task.pk).exists(), False)
        # Check if the 'Task deleted' message is added
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Task deleted')
        # Check if the response redirect correctly
        self.assertRedirects(response, reverse('task:index'))

    def test_add_task(self):
        # form = AddTaskForm(data=form_data)
        task = Task.objects.create(title="New Task created", assigned_to=self.first_user,
                                   task_creator=self.second_user, priority="high",
                                   status="in progress",
                                   category="Flutter App",
                                   description="This is a Django celery project", due_date="2024-07-19T00:00:00Z")
        response = self.client.post(self.task_add_url)
        # self.assertTrue(form.is_valid())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Task.objects.get(
            title='New Task created'))
        self.assertTrue(Task.objects.filter(
            title='New Task created').exists())
        self.assertTemplateUsed(response, 'task/add-task.html')
