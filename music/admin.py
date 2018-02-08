from django.contrib import admin

# Register your models here.
from .models import Course,Student,Album,Song

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Album)
admin.site.register(Song)