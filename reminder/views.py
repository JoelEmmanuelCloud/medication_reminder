from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from .models import Medication

# Create a new chat bot
chatbot_instance = ChatBot('MedicationBot')

# Create a new Trainer for the chat bot
trainer = ChatterBotCorpusTrainer(chatbot_instance)

# Train the chat bot on English language data
trainer.train('chatterbot.corpus.english')

def medication_list(request):
    medications = Medication.objects.all()
    return render(request, 'medication_list.html', {'medications': medications})

@csrf_exempt
def chatbot_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message')

        # Get a response from the chat bot
        bot_response = chatbot_instance.get_response(user_message).text

        return JsonResponse({'bot_response': bot_response})

    return render(request, 'chatbot.html')
