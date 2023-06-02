from django.contrib import admin
from .models import Employee

# Register your models here.
admin.site.register(Employee)

class TagAdmin(admin.ModelAdmin):
    list_display = ('Name')