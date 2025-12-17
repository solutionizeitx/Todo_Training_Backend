from django.db import models


class todomodel(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class list_completed_todo(models.Model):
    todo = models.ForeignKey(todomodel, on_delete=models.CASCADE, related_name="completed_task")
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todo.name