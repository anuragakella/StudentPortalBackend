from django.shortcuts import render
from rest_framework import viewsets
from form_manager.models import Profile, Subject, Question, FeedbackForm
from django.contrib.auth.models import User
from form_manager.serializers import UserSerializer, ProfileSerializer, SubjectSerializer, QuestionSerializer, FeedbackFormSerializer
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action



from rest_framework.response import Response
from rest_framework import generics
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer
    lookup_field = 'username'
    queryset = User.objects.all()

class ShowProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ProfileSerializer
    lookup_field = 'collegeid'
    def get_queryset(self, *args, **kwargs):
        return Profile.objects.all().filter(user__id=self.request.user.id)

class EditUserViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer
    lookup_field = 'username'
    def get_queryset(self, *args, **kwargs):
        return User.objects.all().filter(id=self.request.user.id)

    
class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAdminUser
    ]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

class SubjectViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAdminUser
    ]
    serializer_class = SubjectSerializer
    lookup_field = 'sub_id'
    queryset = Subject.objects.all()

class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAdminUser
    ]
    serializer_class = QuestionSerializer
    lookup_field = 'question_id'
    queryset = Question.objects.all()

class FeedbackFormViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    
    serializer_class = FeedbackFormSerializer
    lookup_field = 'form_id'
    def get_queryset(self, *args, **kwargs):
        print(self.kwargs)
        if('q_id' in self.kwargs):
            return FeedbackForm.objects.all().filter(form_owner__user=self.request.user).filter(question__question_id=self.kwargs['q_id'])
        elif('s_id' in self.kwargs):
            return FeedbackForm.objects.all().filter(form_owner__user=self.request.user).filter(form_child__sub_id=self.kwargs['s_id'])    
        else:
            return FeedbackForm.objects.all().filter(form_owner__user=self.request.user)
    
    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class incompFormsViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    
    serializer_class = FeedbackFormSerializer
    lookup_field = 'form_id'
    def get_queryset(self, *args, **kwargs):
        print(self.kwargs)
        if ('s_id' in self.kwargs):
            return FeedbackForm.objects.all().filter(form_owner__user=self.request.user).filter(form_child__sub_id=self.kwargs['s_id']).filter(editable=True)    
        else:
            return FeedbackForm.objects.all().filter(form_owner__user=self.request.user)
    
    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class completeFormsViewSet(viewsets.ModelViewSet):
    serializer_class = FeedbackFormSerializer
    lookup_field = 'form_id'
    def get_queryset(self, *args, **kwargs):
        print(self.kwargs)
        if ('s_id' in self.kwargs):
            return FeedbackForm.objects.all().filter(form_owner__user=self.request.user).filter(form_child__sub_id=self.kwargs['s_id']).filter(editable=False)    
        else:
            return FeedbackForm.objects.all().filter(form_owner__user=self.request.user)
    
    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminFormViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAdminUser
    ]
    
    serializer_class = FeedbackFormSerializer
    lookup_field = 'form_id'
    def get_queryset(self, *args, **kwargs):
        print(self.kwargs)
        if('q_id' in self.kwargs):
            return FeedbackForm.objects.all().filter(question__question_id=self.kwargs['q_id'])
        elif('s_id' in self.kwargs):
            return FeedbackForm.objects.all().filter(form_child__sub_id=self.kwargs['s_id'])    
        else:
            return FeedbackForm.objects.all()
            
    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompleteAdminFormViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAdminUser
    ]
    
    serializer_class = FeedbackFormSerializer
    lookup_field = 'form_id'
    def get_queryset(self, *args, **kwargs):
        print(self.kwargs)
        if('q_id' in self.kwargs):
            return FeedbackForm.objects.all().filter(question__question_id=self.kwargs['q_id']).filter(editable=False) 
        elif('s_id' in self.kwargs):
            return FeedbackForm.objects.all().filter(form_child__sub_id=self.kwargs['s_id']).filter(editable=False)   
        else:
            return FeedbackForm.objects.all()
            
    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IncompleteAdminFormViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAdminUser
    ]
    
    serializer_class = FeedbackFormSerializer
    lookup_field = 'form_id'
    def get_queryset(self, *args, **kwargs):
        print(self.kwargs)
        if('q_id' in self.kwargs):
            return FeedbackForm.objects.all().filter(question__question_id=self.kwargs['q_id']).filter(editable=True) 
        elif('s_id' in self.kwargs):
            return FeedbackForm.objects.all().filter(form_child__sub_id=self.kwargs['s_id']).filter(editable=True)   
        else:
            return FeedbackForm.objects.all()
            
    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserFilterFormViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAdminUser
    ]
    
    serializer_class = FeedbackFormSerializer
    lookup_field = 'form_id'
    def get_queryset(self, *args, **kwargs):
        print(self.kwargs)
        if('uname' in self.kwargs):
            return FeedbackForm.objects.all().filter(form_owner__user__username=self.kwargs['uname'])
        else:
            return FeedbackForm.objects.all()
            
    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChildFilterFormViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAdminUser
    ]
    
    serializer_class = FeedbackFormSerializer
    lookup_field = 'form_id'
    def get_queryset(self, *args, **kwargs):
        print(self.kwargs)
        if('uname' in self.kwargs):
            print(self.kwargs['uname'])
            return FeedbackForm.objects.all().filter(form_child__subject_owner__user__username=self.kwargs['uname'])
        else:
            return FeedbackForm.objects.all()
            
    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)