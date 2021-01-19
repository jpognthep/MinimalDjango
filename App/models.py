from django.db import models

# Create your models here.
class Todo(models.Model):
    TaskName = models.CharField(max_length=50)
    isComplete = models.BooleanField(default = False)

    def __str__(self):
        return self.TaskName