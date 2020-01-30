from .models import User, Group, Entry
from rest_framework import serializers # Serializers - converts JSON to python object and vice-versa

# RegisterUserSerializer serializes requests to create a new user account
class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# User Serializer 