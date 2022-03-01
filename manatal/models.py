from django.db import models
from django.core.exceptions import ValidationError
import shortuuid

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=20, blank=False, default='')
    address = models.CharField(max_length=128, blank=True)
    students_capacity = models.PositiveSmallIntegerField(blank=False, default=5)

    def students_count(self):
        return Student.objects.filter(school_id=self).count()

    def __str__(self):
        return f"{self.name} ({self.students_count()}/{self.students_capacity} students)"

class Student(models.Model):
    school_id =  models.ForeignKey(School, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=False, default='')
    last_name = models.CharField(max_length=30, blank=False, default='')
    age = models.PositiveSmallIntegerField(blank=True)
    identification = models.CharField(primary_key=True, max_length=20, blank=False, editable=False)

    def save(self, **kwargs):
        if self.school_id.students_count() == self.school_id.students_capacity:
            raise ValidationError("The school is full")
        if not self.identification:
            is_unique = False
            while not is_unique:
                uuid = str(shortuuid.ShortUUID().random(length=20))
                is_unique = not Student.objects.filter(identification=uuid).exists()
            self.identification = uuid
        super(Student, self).save()
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"