from django.db import models

# Create your models here.
class employee(models.Model):
    emp_id = models.CharField(max_length=10)
    emp_name = models.CharField(max_length=30)
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.emp_name
