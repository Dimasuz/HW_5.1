from django.contrib import admin

from .models import Student, Teacher


class TeachersInLine(admin.TabularInline):
    model = Student.teachers.through
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'group',]
    inlines = [TeachersInLine,]
    exclude = ('teachers',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject']
    inlines = [TeachersInLine, ]

