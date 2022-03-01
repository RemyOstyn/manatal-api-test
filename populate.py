import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','manatal_project.settings')

import django
django.setup()

from manatal.models import Student, School
from faker import Faker
import random

fake_generator = Faker()

schools = ['Django School', 'Python School', 'SQL School']

def get_school():
    address = fake_generator.address()
    school = School.objects.get_or_create(name=random.choice(schools))[0]
    while school.students_count() == school.students_capacity:
        school = School.objects.get_or_create(name=random.choice(schools))[0]
    if school.address == "":
        school.address = address
    school.save()
    return school

def populate(n):
    for i in range(n):
        school = get_school()
        first_name = fake_generator.first_name()
        last_name = fake_generator.last_name()
        age = random.randint(18,30)
        Student.objects.get_or_create(school_id=school, first_name=first_name, last_name=last_name, age=age)[0]

if __name__ == '__main__':
    print('Lauching populating script')
    populate(15)
    print('Populating Script completed')