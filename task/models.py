from django.db import models
from account.models import User
from django.urls import reverse


class Task(models.Model):
    STATUS_CHOICES = (
        ('in progress', 'in progress'),
        ('completed', 'Completed'),
        ('overdue', 'Overdue')
    )
    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    )
    task_creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Task_Manager")
    assigned_to = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    priority = models.CharField(
        max_length=15, choices=PRIORITY_CHOICES)
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES)
    category = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()

    class Meta:
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return reverse("task:task-details", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("task:task-update", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
