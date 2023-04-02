from django.db import models
from django.apps import apps

app_label = apps.get_containing_app_config(__name__).name

class UserData(models.Model):
    class Meta:
        app_label = app_label
    uploaded_file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
