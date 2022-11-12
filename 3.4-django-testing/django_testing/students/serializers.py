from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django_testing.settings import MAX_STUDENTS_PER_COURSE
from students.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate(self, attrs):
        num_students = len(attrs.get('students')) if attrs.get('students') else 0
        print(attrs['name'])
        count_students = 0
        try:
            count_students = Course.objects.get(name=attrs['name']).students.count()
        except Exception:
            pass
        if num_students + count_students > MAX_STUDENTS_PER_COURSE:
            raise ValidationError('Превышено количество студентов на курсе')
        return attrs

