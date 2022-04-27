from django.views.generic import ListView
from users.models import User


class UserListView(ListView):
    model = User
    template_name = 'listview.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context
