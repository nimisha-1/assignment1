from django.db import models


# Create your models here.
class Emp_details(models.Model):
    emp_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone_num = models.IntegerField(max_length=20)


    def __str__(self):
        return self.first_name
