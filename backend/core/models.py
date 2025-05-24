from django.db import models

class Submission(models.Model):
    user_input = models.TextField()
    summary = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
