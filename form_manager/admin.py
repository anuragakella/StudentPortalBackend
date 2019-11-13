from django.contrib import admin
from form_manager import models as fmdls
admin.site.register(fmdls.Profile)
admin.site.register(fmdls.Subject)
admin.site.register(fmdls.Question)
admin.site.register(fmdls.FeedbackForm)

