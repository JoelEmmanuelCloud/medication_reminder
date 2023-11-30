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


# Add this function at the end of your views.py file
def simulate_chatbot_response(user_message):
    responses = [
        "Hello, how can I assist you?",
        "I'm here to help with your medication. What do you need?",
        "Tell me more about your medication schedule.",
        "If you have any questions about your medication, feel free to ask.",
    ]
    return random.choice(responses)
