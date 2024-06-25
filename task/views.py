from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from .forms import AddTaskForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, FormView, View, RedirectView
from django.contrib import messages
from .models import Task
# Create your views here.


class Index(TemplateView):
    template_name = 'task/index.html'

    def get_context_data(self, **kwargs):
        tasks = Task.objects.all()
        context = super().get_context_data(**kwargs)
        context['tasks'] = tasks
        context['title'] = 'Task Management'
        context['addtaskform'] = AddTaskForm
        return context


class AddTask(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = AddTaskForm
    template_name = 'task/add-task-form.html'
    success_message = 'Task added'

    def form_valid(self, form):
        # form.instance.user = self.request.user
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

    def form_valid(self, form):
        # form.instance.user = self.request.user
        return super().form_valid(form)

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
