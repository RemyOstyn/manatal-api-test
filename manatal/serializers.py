from rest_framework import serializers 
from manatal.models import School, Student

# School Serializer
class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ['id','name','address','students_capacity']

# Student Serializer
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['identification', 'school_id', 'first_name', 'last_name','age']