from django.urls import path
from .views import medication_list, chatbot

urlpatterns = [
    path('list/', medication_list, name='medication_list'),
    path('chatbot/', chatbot, name='chatbot')
]
