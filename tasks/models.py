from django.db import models
from django.contrib.auth import get_user_model

class Task(models.Model):
    name = models.CharField(max_length=256)
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    desc=models.TextField(blank=True)

    def __str__(self):
        return self.name