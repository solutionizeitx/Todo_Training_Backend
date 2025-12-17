from django.db import models

class Todo_item(models.Model):
    name = models.CharField(max_length= 100)
    description = models.TextField()
    is_completed = models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.name