"""CRM Views Files"""
from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.urls import path
from .models import Task
from .forms import TaskForm


def homepage(request):
    """Home Page View"""
    return render(request, 'crm/index.html')


def tasks(request):
    """Task View"""
    queryDataAll = Task.objects.all()
    context = {"AllTasks": queryDataAll}
    return render(request, 'crm/view-tasks.html', context)


def register(request):
    """Registration Page View"""
    return render(request, 'crm/register.html')


def create_task(request):
    """Model Task Form View"""
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view-tasks')

    context = {'TaskForm': form}
    return render(request, 'crm/create-task.html', context)


def update_task(request, pk):
    """View to Update a Task"""
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('view-tasks')

    context = {'UpdateTask': form}
    return render(request, 'crm/update-task.html', context)


def delete_task(request, pk):
    """Delete a Task View"""
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('view-tasks')
    return render(request, 'crm/delete-task.html')
