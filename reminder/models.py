from django.db import models
from datetime import datetime, timedelta

class Medication(models.Model):
    name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=20, choices=[('daily', 'Daily'), ('weekly', 'Weekly')], default='daily')
    start_date = models.DateField(default=datetime.now)
    
    def __str__(self):
        return self.name

    class Meta:
        app_label = 'reminder'

class Reminder(models.Model):
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    reminder_time = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    next_reminder_time = models.DateTimeField(default=datetime.now)
    
    def save(self, *args, **kwargs):
        if not self.next_reminder_time:
            self.next_reminder_time = datetime.now() + timedelta(days=1)
        super().save(*args, **kwargs)