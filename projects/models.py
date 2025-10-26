from django.db import models 
from django.conf import settings 
user_model = settings.AUTH_USER_MODEL

# Create your models here.


class ProjectStatus(models.IntegerChoices):
    PENDING = 1, 'Pending'
    COMPLETED = 2, 'Completed'
    POSTPONED = 3, 'Postponed'
    CANCELLED = 4, 'Cancelled'

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.IntegerField(choices=ProjectStatus.choices,default=ProjectStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(user_model, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    

class Task(models.Model):
    descrtiption = models.TextField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)

    def __str__(self):
        return self.description