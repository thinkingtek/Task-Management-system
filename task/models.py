from django.db import models
from account.models import User


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
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    priority = models.CharField(
        max_length=15, choices=PRIORITY_CHOICES)
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES)
    category = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField(editable=True)
