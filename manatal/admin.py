from django.contrib import admin
from .models import School, Student

# Register models to have access to it on admin page
admin.site.register(School)
admin.site.register(Student)