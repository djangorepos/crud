from rest_framework import status
from rest_framework.fields import CharField, IntegerField
from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from users.models import User


class UserCreateSerializer(ModelSerializer):
    password = CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'type', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserUpdateSerializer(ModelSerializer):
    id = IntegerField(min_value=1)
    password = CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'type', 'password')


class UserDeleteSerializer(ModelSerializer):

    @staticmethod
    def delete(request, pk):
        print(request)
        return User.objects.get(id=pk)

    class Meta:
        model = User
        fields = ('id',)
