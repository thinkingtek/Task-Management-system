from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from .forms import AddTaskForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, FormView, View, RedirectView
# Create your views here.


class Index(TemplateView):
    template_name = 'task/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Task Management'
        context['addtaskform'] = AddTaskForm
        return context
