from django.db import models
from django.conf import settings

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='first_name', null=False)
    last_name = models.CharField(max_length=50, verbose_name='last_name', null=False)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=11, default=+7)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='employee_user',
        null=True
    )
    def __str__(self):
        return self.first_name + self.last_name