from django.db import models

class Todo_list(models.Model):
    task = models.CharField(max_length=100)
    finished = models.BooleanField(default=False)
    description = models.BooleanField(default=False)
