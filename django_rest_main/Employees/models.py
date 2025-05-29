from django.db import models

# Create your models here.
class employee(models.Model):
    emp_id = models.CharField(10)
    emp_name = models.CharField(30)
    designation = models.CharField(50)

    def __str__(self):
        return self.emp_name
