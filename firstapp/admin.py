# from django.contrib import admin

# # Register your models here.
# from firstapp.models import Student
# admin.site.register(Student)

from django.contrib import admin
from .models import course

# Register your models here.

admin.site.register(course)
