from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions

User = get_user_model()


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "phone_no", "password"]

    def validate(self, data):
        """Use to validate the password during registering the user.

        Args:
            data (dict): A dictionary containing user data, including the password.

        Raises:
            Exception.ValidationError: If the password fails the validation criteria.

        Returns:
            dict: The original data dictionary if validation is successful.
        """

        user = User(**data)
        password = data.get("password")

        try:
            validate_password(password, user)
        except exceptions.ValidationError as e:
            serializers_errors = serializers.as_serializer_error(e)
            raise Exception.ValidationError(
                {"password": serializers_errors["non_field_error"]}
            )

        return data

    def create_user(self, validated_data):
        """Create a user instance in the database using validated data.

        This method leverages the serializers in Django Rest Framework (DRF)
        to create a user with the provided validated data.

        Args:
            validated_data (dict): The data that has been validated

        Returns:
            user: Returns the instance of the user
        """

        user = User.objects.create_user(
            email=validated_data["email"],
            username=validated_data["username"],
            phone_no=validated_data["phone_no"],
            password=validated_data["password"],
        )

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'phone_no']