from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    collegeid = models.CharField(max_length=10)
    is_prof = models.BooleanField(default=False)

    def __str__(self):
        ret = "prof" if self.is_prof else "student"
        return self.user.username + "-" + ret

class Subject(models.Model):
    subject_owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    sub_id = models.AutoField(primary_key=True)
    sub_name = models.CharField(max_length=50)

    def __str__(self):
        return self.sub_name + "-" + self.subject_owner.user.username

class Question(models.Model):
    Q_TYPES = [
        ('SLDR', 'Slider/ Rating'),
        ('BOOL', 'Boolean Question'),
        ('TEXT', 'Text Based Question'),
        ('MULC', 'Multiple Choice Question')
    ]
    question_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=200)
    question_type = models.CharField(max_length=4, choices=Q_TYPES, default='SLDR')
    def __str__(self):
        return str(self.question_id) + "-" + self.question_type
    
class FeedbackForm(models.Model):
    form_id = models.AutoField(primary_key=True)
    form_owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    form_child = models.ForeignKey(Subject, on_delete=models.CASCADE)
    form_answer = models.TextField(null = True, blank=True)
    editable = models.BooleanField(default=True)
    def __str__(self):
        return self.form_owner.user.username + "-" + self.form_child.sub_name + "-" + str(self.question.question_id)
    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def new_user_handler(sender, instance=None, created=False, **kwargs):
    if(created and instance.is_staff == False):
       Profile.objects.create(user=instance, collegeid = "18VF1M33--", is_prof=True)
       for t_id in range(1, 8):
            for q_id in range(1, 8):
                 FeedbackForm.objects.create(
                    form_owner = instance.profile, 
                    question = Question.objects.all().filter(question_id=q_id)[0], 
                    form_child = Subject.objects.all().filter(sub_id=t_id)[0], 
                    form_answer=""
                    )