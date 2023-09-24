from django.forms import ModelForm
from . models import Task


class TaskForm(ModelForm):
    """Metadata"""
    class Meta:
        model = Task
        fields = '__all__'
