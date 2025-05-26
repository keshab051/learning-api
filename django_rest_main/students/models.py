from django.db import models

class student(models.Model):
    
    def __str__(self):
        return self.name;

    student_id =models.CharField(max_length=10)
    name =models.CharField(max_length=50)
    branch =models.CharField(max_length=50)
# Create your models here.
