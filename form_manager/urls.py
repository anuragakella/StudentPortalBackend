from django.urls import path, include
from form_manager import views
from rest_framework import routers
from form_manager.routes import FormRouter

router = routers.DefaultRouter()
router.register(r'super/profiles', views.ProfileViewSet, basename='profiles')
router.register(r'super/subjects', views.SubjectViewSet, basename='subjects')
router.register(r'super/questions', views.QuestionViewSet, basename='questions')
router.register(r'super/users', views.UserViewSet, basename='users')
router.register(r'forms', views.FeedbackFormViewSet, basename='forms')
router.register(r'forms/filters/question/(?P<q_id>.+)', views.FeedbackFormViewSet, basename='forms-filter-questions')
router.register(r'forms/filters/subject/(?P<s_id>.+)', views.FeedbackFormViewSet, basename='forms-filter-subjects')
router.register(r'super/forms', views.AdminFormViewSet, basename='forms')
router.register(r'super/forms/filters/question/(?P<q_id>.+)', views.AdminFormViewSet, basename='forms-filter-questions')
router.register(r'super/forms/filters/subject/(?P<s_id>.+)', views.AdminFormViewSet, basename='forms-filter-subjects')
router.register(r'forms/filters/subjectState/incomplete/(?P<s_id>.+)', views.incompFormsViewSet, basename='forms-filter-subjects')
router.register(r'forms/filters/subjectState/complete/(?P<s_id>.+)', views.completeFormsViewSet, basename='forms-filter-subjects')
router.register(r'super/forms/filters/subjectState/incomplete/(?P<s_id>.+)', views.IncompleteAdminFormViewSet, basename='forms-filter-subjects')
router.register(r'super/forms/filters/subjectState/complete/(?P<s_id>.+)', views.CompleteAdminFormViewSet, basename='forms-filter-subjects')
router.register(r'super/form_filter/(?P<uname>.+)', views.UserFilterFormViewSet, basename='forms-filter-subjects')
router.register(r'super/prof_filter/(?P<uname>.+)', views.ChildFilterFormViewSet, basename='forms-filter-subjects')
router.register(r'me', views.ShowProfileViewSet, basename='auth-user-profile')
router.register(r'edit', views.EditUserViewSet, basename='auth-user-profile-edit')

urlpatterns = [
    path('', include(router.urls)),
]