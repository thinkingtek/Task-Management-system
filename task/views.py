from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from .forms import AddTaskForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, FormView, View, RedirectView
from django.contrib import messages
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# API VIEWS


@api_view(["GET"])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["PUT"])
def taskUpdate(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def taskDelete(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    task.delete()
    return Response("Item successfully deleted")


@api_view(["GET"])
def taskDetails(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


# NORMAL DJANGO VIEWS

class Index(TemplateView):
    template_name = 'task/index.html'

    def get_context_data(self, **kwargs):
        tasks = Task.objects.all()
        context = super().get_context_data(**kwargs)
        context['inprogress_tasks'] = tasks.filter(status="in progress")
        context['overdue_tasks'] = tasks.filter(status="overdue")
        context['completed_tasks'] = tasks.filter(status="completed")
        context['tasks'] = tasks
        context['title'] = 'Task Management'
        context['addtaskform'] = AddTaskForm
        return context


class AddTask(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = AddTaskForm
    template_name = 'task/add-task.html'
    success_message = 'Task added'

    def form_valid(self, form):
        form.instance.task_creator = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks_active"] = True
        context['title'] = 'Add Task'
        context['submit_btn'] = 'Submit'
        return context


class UpdateTask(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = AddTaskForm
    template_name = 'task/update-task.html'
    success_message = 'Task Updated'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_active"] = True
        context['title'] = 'Update Task'
        context['submit_btn'] = 'Update'
        return context


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task/task-details.html'

    def get_context_data(self, **kwargs):
        task = self.get_object()
        context = super().get_context_data(**kwargs)
        context['title'] = f'Task | {task.title}'
        context['addtaskform'] = AddTaskForm
        return context


def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    messages.info(request, f'Task deleted')
    return redirect('task:index')
