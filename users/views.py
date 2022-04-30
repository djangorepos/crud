from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from users.forms import UserForm
from users.models import User


def list_view(request):
    return render(request, 'base.html', {'users': User.objects.all()})


def create_view(request):
    context = {}
    form = UserForm()
    context['users'] = User.objects.all()
    context['form'] = form

    if request.method == 'POST':
        form = UserForm(request.POST)
        context['form'] = form
        if form.is_valid():
            user = form.instance
            user.set_password(form.cleaned_data["password1"])
            if user.type == 'Admin':
                user.is_superuser = True
                user.is_staff = True
            else:
                user.is_staff = True
            user.save()
            messages.success(request, "User registered.")
        else:
            context['error'] = True
            messages.error(request, "Error, something is wrong")

            return render(request, 'create-view.html', context)

    return render(request, 'create-view.html', context)


def edit_view(request, pk):
    context = {}
    user = User.objects.get(id=pk)
    form = UserForm(instance=user)
    context['form'] = form
    context['users'] = User.objects.all()
    context['user'] = user

    if request.method == 'POST':
        form = UserForm(request.POST)
        context['form'] = form
        if form.is_valid():
            if user.username != form.instance.username:
                user.username = form.instance.username
            user.first_name = form.instance.first_name
            user.last_name = form.instance.last_name
            user.email = form.instance.email
            user.type = form.instance.type
            user.set_password(form.cleaned_data["password1"])

            if user.type == 'Admin':
                user.is_superuser = True
                user.is_staff = True
            else:
                user.is_superuser = False
                user.is_staff = True

            user.save()
            messages.success(request, "User edited.")
        else:
            context['error'] = True
            messages.error(request, "Error, something is wrong")
            return render(request, 'edit-view.html', context)

    return render(request, 'edit-view.html', context)


def delete_view(request, pk):
    User.objects.get(id=pk).delete()
    messages.success(request, "User deleted.")
    return redirect(reverse('list_view'))
