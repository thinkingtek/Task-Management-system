from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, FormView, View, RedirectView
# Create your views here.


class Index(TemplateView):
    template_name = 'task/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Task Management'
        # context['editors_first'] = editors_first
        # context['editors_pick'] = editors_pick
        # context['trending_posts'] = trending_posts
        # context['latest_posts'] = latest_posts
        # context["home_active"] = True
        return context
