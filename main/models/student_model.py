from django.db import models
import uuid
from .school_model import School

class Student(models.Model):
    identification_string = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=45, null=False)
    last_name = models.CharField(max_length=45, null=False)
    gpa = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    school = models.ForeignKey(
        School, related_name='students',
        on_delete=models.CASCADE)