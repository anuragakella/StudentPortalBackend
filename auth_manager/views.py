from django.shortcuts import render
from rest_framework import viewsets, generics
from form_manager.models import Profile, Subject, Question, FeedbackForm
from django.contrib.auth.models import User
from auth_manager.serializers import RegisterSerializer
from form_manager.serializers import UserSerializer
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data
        })

class LogoutView(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)