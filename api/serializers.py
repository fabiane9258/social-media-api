from rest_framework import serializers
from .models import User, Post
from django.contrib.auth.password_validation import validate_password

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)  # For password confirmation

    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'bio', 'profile_picture_url', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data.get('role', 'regular'),
            bio=validated_data.get('bio', ''),
            profile_picture_url=validated_data.get('profile_picture_url', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'author', 'author_username', 'content', 'created_at']
        read_only_fields = ['author', 'created_at']