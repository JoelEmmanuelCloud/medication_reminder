from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Medication, Reminder
from datetime import datetime, timedelta
from .responses import get_response
from .forms import ReminderForm, MedicationForm, CustomUserCreationForm



def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logout successful!')
    return redirect('home')

@login_required
def update_medication_reminder(request, reminder_id):
    reminder = get_object_or_404(Reminder, pk=reminder_id)

    if request.method == 'POST':
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            return redirect('medication_list') 
    else:
        form = ReminderForm(instance=reminder)

    return render(request, 'update_medication_reminder.html', {'form': form, 'reminder': reminder})

@login_required
def medication_list(request):
    medications = Medication.objects.all()
    return render(request, 'medication_list.html', {'medications': medications})

@login_required
@csrf_exempt
def chatbot_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message')

        if 'update reminders' in user_message.lower():
            update_medication_reminders()

        bot_response = get_response(user_message)

        return JsonResponse({'bot_response': bot_response})

    return render(request, 'chatbot.html')

@login_required
def update_medication_reminders():
    # Logic to update medication reminders
    medications = Medication.objects.all()

    for medication in medications:
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

@login_required
def medication_detail(request, medication_id):
    medication = get_object_or_404(Medication, pk=medication_id)
    reminders = medication.reminder_set.all()

    if request.method == 'POST':
        
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.medication = medication
            reminder.save()
            return redirect('medication_detail', medication_id=medication_id)
    else:
        form = ReminderForm()

    return render(request, 'medication_detail.html', {'medication': medication, 'reminders': reminders, 'form': form})

def delete_medication_reminder(request, reminder_id):
    reminder = get_object_or_404(Reminder, pk=reminder_id)
    medication_id = reminder.medication.id
    reminder.delete()
    return redirect('medication_detail', medication_id=medication_id)

@login_required
def add_medication_reminder(request, medication_id):
    medication = get_object_or_404(Medication, pk=medication_id)

    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.medication = medication
            reminder.save()
            return redirect('medication_detail', medication_id=medication_id)
    else:
        form = ReminderForm()

    return render(request, 'add_medication_reminder.html', {'form': form, 'medication': medication})


@login_required
def add_medication(request):
    if request.method == 'POST':
        form = MedicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medication_list')
    else:
        form = MedicationForm()

    return render(request, 'add_medication.html', {'form': form})
