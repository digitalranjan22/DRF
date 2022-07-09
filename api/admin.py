from django.contrib import admin
from .models import Student
from .models import Project

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display =['id','name','roll','city']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display =['id','ProjectName','ProjectStatus','Department','ClientName','Technology','StartDate','EndDate','EstimatedHours']
