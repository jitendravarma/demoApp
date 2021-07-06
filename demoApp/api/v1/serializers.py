from core.models import BaseUserProfile, Text
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = BaseUserProfile
        fields = ('id', 'email', 'first_name', 'last_name')


class TextSerializer(ModelSerializer):
    class Meta:
        model = Text
        fields = ('id', 'data_id', 'user_id', 'title', 'body')
