from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True)
    title = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    desc = models.TextField(null=True, blank = True)

    def __str__(self):
        return f"{self.user.username}" + " - " + f"{self.title}"
