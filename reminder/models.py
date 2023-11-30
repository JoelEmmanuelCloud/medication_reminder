# reminder/models.py
from django.db import models

class Medication(models.Model):
    name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=50)

class Reminder(models.Model):
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    reminder_time = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
