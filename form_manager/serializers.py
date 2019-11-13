from form_manager.models import Profile, Subject, Question, FeedbackForm
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(UserSerializer, self).__init__(*args, **kwargs)
    lookup_field = 'username'

    class Meta:
        model = User
        fields = ['is_staff', 'username', 'first_name', 'last_name']

    def update(self, instance, validated_data):
        # instance.id = validated_data['id']
        # instance.username = validated_data['username']
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        print(instance)
        instance.save()
        return instance


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Profile
        fields = ['user', 'collegeid', 'is_prof']

class UnameSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Profile
        fields = ['collegeid', 'user']

class SubjectSerializer(serializers.ModelSerializer):
    lookup_field = 'sub_id'
    subject_owner = ProfileSerializer(required=True)

    class Meta:
        model = Subject
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    lookup_field = 'question_id'

    class Meta:
        model = Question
        fields = "__all__"


class FeedbackFormSerializer(serializers.ModelSerializer):
    form_owner = UnameSerializer(required=True)
    question = QuestionSerializer(required=True)
    form_child = SubjectSerializer(required=True)
    form_answer = serializers.CharField(required=False, allow_blank=True)
    lookup_field = 'form_id'

    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(FeedbackFormSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = FeedbackForm
        fields = ['form_id', 'form_owner',
                  'question', 'form_child', 'form_answer', 'editable']

    def update(self, instance, validated_data):
        # print(instance.form_owner)
        print(validated_data)
        instance.form_answer = validated_data['form_answer']
        instance.editable = validated_data['editable']
        instance.save()
        return instance

    def create(self, validated_data):
        form = FeedbackForm(
            form_answer=validated_data['form_answer'],
            question=validated_data['question'],
            form_child=validated_data['form_child']
        )
        form.save(form_owner=self.request.user)
        return form
