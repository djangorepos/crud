from django.contrib import messages
from django.shortcuts import render
from users.forms import UserForm
from users.models import User


def user_view(request):
    context = {}
    form = UserForm()
    context['users'] = User.objects.all()
    context['form'] = form

    if request.method == 'POST':
        form = UserForm(request.POST)
        context['form'] = form
        if form.is_valid():
            print('form valid')
            form.save()
            messages.success(request, "Congratulations, you are now a registered user!")
            context['success'] = True
        else:
            print('form invalid')
            context['success'] = False
            messages.error(request, "Error, something is wrong")

            return render(request, 'view.html', context)

    return render(request, 'view.html', context)
