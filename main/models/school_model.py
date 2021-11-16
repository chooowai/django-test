from django.db import models

class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False)
    max_student = models.PositiveIntegerField()