from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserForm(UserCreationForm):

    """ def __init__(self, *args, **kwargs):
         super(UserForm, self).__init__(*args, **kwargs)
         for field_name, field in self.fields.items():
             field.widget.attrs['class'] = 'form-control """

    class Meta:
        model = User
        fields = 'username', 'first_name', 'last_name', 'email', 'type'
