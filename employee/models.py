from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='first_name', null=False)
    last_name = models.CharField(max_length=50, verbose_name='last_name', null=False)
    
    phone = models.CharField(max_length=11, default=+7)

    def __str__(self):
        return self.first_name + self.last_name