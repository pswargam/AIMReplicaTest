from django.contrib import admin

# Register your models here.
from .models import Courses,Students

admin.site.register(Courses);
admin.site.register(Students);