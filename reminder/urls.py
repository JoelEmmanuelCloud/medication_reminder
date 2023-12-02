from django.urls import path
from .views import medication_list, chatbot_view

urlpatterns = [
    path('medication/', medication_list, name='medication_list'),
    path('chatbot/', chatbot_view, name='chatbot')
]
