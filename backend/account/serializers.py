from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import ContractorAccount, User, CustomerAccount


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                username=email, password=password)
            if not user:
                msg = 'Access denied: wrong email or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "email" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')

        attrs["user"] = user

        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "last_name", "first_name", "patronymic", "is_contractor", "is_customer"]


class ContractorAccountSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(label="E-mail", write_only=True)
    password = serializers.CharField(label="Пароль", write_only=True)
    first_name = serializers.CharField(label="Имя", write_only=True)
    last_name = serializers.CharField(label="Фамилия", write_only=True)
    patronymic = serializers.CharField(label="Отчество", write_only=True, required=False)
    user = UserSerializer(read_only=True)

    class Meta:
        model = ContractorAccount
        fields = ["user", "id", "first_name", "last_name", "patronymic", "email", "password", "TIN", "short_title", "position", "phone_number"]

    def create(self, validated_data):
        return ContractorAccount.objects.create(**validated_data)


class CustomerAccountSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(label="E-mail", write_only=True)
    password = serializers.CharField(label="Пароль", write_only=True)
    first_name = serializers.CharField(label="Имя", write_only=True)
    last_name = serializers.CharField(label="Фамилия", write_only=True)
    patronymic = serializers.CharField(label="Отчество", write_only=True, required=False)
    user = UserSerializer(read_only=True)

    class Meta:
        model = CustomerAccount
        fields = ["user", "id", "first_name", "last_name", "patronymic", "email", "password", "department", "position", "phone_number"]

    def create(self, validated_data):
        return CustomerAccount.objects.create(**validated_data)
