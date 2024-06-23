from django import forms
from .models import *


class AddTaskForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Task
        fields = "__all__"
        # exclude = ('user', 'timestamp')
        widgets = {
            'description': forms.Textarea(attrs={
                'placeholder': "A short description of the project"
            })
        }
