from django.urls import path
from .views import (
    home,
    medication_list,
    add_medication,
    chatbot_view,
    medication_detail,
    delete_medication_reminder,
    add_medication_reminder,
    update_medication_reminder,
    register,
    user_login,
    user_logout,
)


urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('medication/', medication_list, name='medication_list'),
    path('add_medication/', add_medication, name='add_medication'),
    path('chatbot/', chatbot_view, name='chatbot'),
    path('medication_detail/<int:medication_id>/', medication_detail, name='medication_detail'),
    path('delete_medication_reminder/<int:reminder_id>/', delete_medication_reminder, name='delete_medication_reminder'),
    path('add_medication_reminder/<int:medication_id>/', add_medication_reminder, name='add_medication_reminder'),
    path('update_medication_reminder/<int:reminder_id>/', update_medication_reminder, name='update_medication_reminder'),  # Correct import statement
]
