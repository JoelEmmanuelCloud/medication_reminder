# reminder/management/commands/update_reminders.py
from django.core.management.base import BaseCommand
from datetime import datetime, timedelta  # Add this import
from reminder.models import Reminder, Medication

class Command(BaseCommand):
    help = 'Update medication reminders'

    def handle(self, *args, **options):
        medications = Medication.objects.all()

        for medication in medications:
            # Logic to calculate the next reminder time based on frequency, start_date, etc.
            # For simplicity, let's assume a daily reminder for demonstration purposes.
            next_reminder_time = medication.start_date

            while next_reminder_time <= datetime.now():
                next_reminder_time += timedelta(days=1)

            # Update or create a new reminder record with the calculated next reminder time.
            reminder, created = Reminder.objects.update_or_create(
                medication=medication,
                defaults={
                    'reminder_time': next_reminder_time,
                    'next_reminder_time': next_reminder_time,
                }
            )
