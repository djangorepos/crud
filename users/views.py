from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.mixins import DestroyModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.forms import UserCreateForm, UserUpdateForm
from users.serializers import *


def list_view(request):
    return render(request, 'base.html', {'users': User.objects.all()})


def create_view(request):
    context = {}
    form = UserCreateForm()
    context['users'] = User.objects.all()
    context['form'] = form

    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        context['form'] = form

        if form.is_valid():
            form.save()
            messages.success(request, "User registered.")
        else:
            context['error'] = True
            messages.error(request, "Error, something is wrong")

    return render(request, 'create-view.html', context)


def update_view(request, pk):
    context = {}
    user = User.objects.get(id=pk)
    form = UserUpdateForm(instance=user)
    context['form'] = form
    context['users'] = User.objects.all()
    context['user'] = user

    if request.method == 'POST':
        form = UserUpdateForm(request.POST)
        context['form'] = form

        if form.is_valid():
            user.save()
            messages.success(request, "User updated.")
        else:
            context['error'] = True
            messages.error(request, "Error, something is wrong")

    return render(request, 'update-view.html', context)


def delete_view(request, pk):
    User.objects.get(id=pk).delete()
    messages.success(request, "User deleted.")
    return redirect(reverse('list_view'))


class UserCreateAPIView(GenericAPIView):
    """
    Registers a new user.
    """
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer

    def post(self, request):
        """
        Creates a new User object.
        All fields are required.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class UserUpdateAPIView(RetrieveUpdateAPIView):
    """
    Updates user.
    """
    permission_classes = [AllowAny]
    serializer_class = UserUpdateSerializer

    def get(self, request, *args, **kwargs):
        return Response({"detail": "Method \"GET\" not allowed."},
                        status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        """
        Updates User object.
        All fields are required.
        """
        user = User.objects.get(id=request.data['id'])
        serializer = self.serializer_class(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDeleteAPIView(GenericAPIView, DestroyModelMixin):
    """
    Deletes user.
    """
    permission_classes = [AllowAny]
    serializer_class = UserDeleteSerializer

    def delete(self, request, pk):
        instance = self.serializer_class.delete(request, pk)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
