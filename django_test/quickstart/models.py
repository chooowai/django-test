from os import name
from django.db import models
import uuid
# Create your models here.
class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False)
    max_student = models.PositiveIntegerField()

class Student(models.Model):
    identification_string = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=45, null=False)
    last_name = models.CharField(max_length=45, null=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE)