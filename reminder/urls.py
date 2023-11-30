from django.urls import path
from .views import medication_list

urlpatterns = [
    path('list/', medication_list, name='medication_list'),
]
