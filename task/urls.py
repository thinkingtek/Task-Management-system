from django.urls import path
from .views import *

app_name = 'task'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('add-task/', AddTask.as_view(), name='add-task'),
    path('task-details/<int:pk>/', TaskDetail.as_view(), name='task-details'),
    path('task-update/<int:pk>/', UpdateTask.as_view(), name='task-update'),
    path('delete-task/<int:pk>/delete/', deleteTask, name='task-delete'),
]
