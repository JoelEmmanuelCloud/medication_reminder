from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
import openai
from .models import Medication

# Set your OpenAI API key
openai.api_key = 'your_openai_api_key'

def medication_list(request):
    medications = Medication.objects.all()
    return render(request, 'medication_list.html', {'medications': medications})

@csrf_exempt
def chatbot_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message')

        # Make a request to the ChatGPT API
        chatgpt_response = generate_chatgpt_response(user_message)

        # Extract the bot response from the ChatGPT API response
        bot_response = chatgpt_response['choices'][0]['text']

        return JsonResponse({'bot_response': bot_response})

    return render(request, 'chatbot.html')

def generate_chatgpt_response(user_message):
    # Make a request to the ChatGPT API
    response = openai.Completion.create(
        engine="text-davinci-003",  # Specify the ChatGPT engine
        prompt=user_message,
        max_tokens=100,
    )
    return response
