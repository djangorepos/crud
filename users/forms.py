from django.contrib.auth.forms import UserCreationForm


from .models import User


class UserCreateForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['required'] = 'required'

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'type',)


class UserUpdateForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['required'] = 'required'

    def clean(self):
        cleaned_data = super().clean()
        if User.objects.exclude(id=self.instance.id).filter(
                is_active=True, username=cleaned_data.get('username')).exists():
            self._validate_unique = False
        else:
            self._validate_unique = True
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'type',)
