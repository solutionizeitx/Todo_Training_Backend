from django.db import models
from django.contrib.auth.models import User

class Todo_item(models.Model):
    name = models.CharField(max_length= 100)
    description = models.TextField()
    is_completed = models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add= True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null= True, blank= True)

    def __str__(self):
        return self.name