from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from users.forms import UserForm
from users.models import User


def user_view(request):
    context = {}
    form = UserForm()
    context['users'] = User.objects.all()
    context['form'] = form

    if request.method == 'POST':

        if form.is_valid():
            print('form valid')
            form.save()

        else:
            print('form valid')
            print(form.errors)
            context['form'] = form
            return render(request, 'view.html', context)

    return render(request, 'view.html', context)


class UserView(ListView, CreateView):
    model = User
    form_class = UserForm
    template_name = 'view.html'
    paginate_by = 10

    def __init__(self):
        super().__init__()
        self.object = None

    def get_context_data(self, **kwargs):
        object_list = User.objects.all()
        context = super().get_context_data(**kwargs)
        context['users'] = object_list
        return context

    def get_success_url(self):
        messages.success(
            self.request, 'User has been created successfully.')
        return reverse_lazy("listview")
