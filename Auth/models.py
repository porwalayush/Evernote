from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TODO(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    Task=models.CharField(max_length=100)
    Task_Description = models.TextField(blank=True)
    Important = models.BooleanField()
    def __str__(self):
        return str(self.user)
