"""CRM Views Files"""
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.urls import path
from .models import Task
from .forms import TaskForm, CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')
    context = {'Registration': form}

    return render(request, 'crm/register.html', context)


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


def my_login(request):
    """Account Login View"""
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

    context = {'LoginForm': form}
    return render(request, 'crm/my-login.html', context)


@login_required(login_url='my-login')
def dashboard(request):
    """Member Dashboard View"""
    return render(request, 'crm/dashboard.html')


def user_logout(request):
    """Member Logout View"""
    auth.logout(request)
    return redirect("")
