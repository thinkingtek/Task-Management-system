from django.urls import path
from .views import *

app_name = 'task'

urlpatterns = [
    path('', Index.as_view(), name='index'),

    # api's
    path('api-task-list/', task_list, name='task-list'),
    path('api-task-create/', taskCreate, name='task-create'),
    path('api-task-details/<int:pk>/',
         taskDetails, name='api-task-details'),
    path('api-task-update/<int:pk>/', taskUpdate, name='api-task-update'),
    path('api-task-delete/<int:pk>/', taskDelete, name='api-task-delete'),

    # Normal view
    path('add-task/', AddTask.as_view(), name='add-task'),
    path('task-details/<int:pk>/', TaskDetail.as_view(), name='task-details'),
    path('task-update/<int:pk>/', UpdateTask.as_view(), name='task-update'),
    path('delete-task/<int:pk>/delete/', deleteTask, name='task-delete'),
]
