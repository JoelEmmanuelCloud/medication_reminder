from django.shortcuts import render
from django.http import JsonResponse
from .models import Medication
import random

def medication_list(request):
    medications = Medication.objects.all()
    return render(request, 'medication_list.html', {'medications': medications})

def chatbot(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message')

        # Simulate a chatbot response (replace this with your actual chatbot logic)
        bot_response = simulate_chatbot_response(user_message)

        return JsonResponse({'bot_response': bot_response})

    return render(request, 'chatbot.html')
