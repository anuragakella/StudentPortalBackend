from form_manager.models import Profile, Subject, Question, FeedbackForm
from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password' : {'write_only': True}}
    
    def create(self, validated_data):
        return User.objects.create_user(username=validated_data['username'], password=validated_data['password'])