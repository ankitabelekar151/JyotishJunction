# voice_calling/urls.py

from django.urls import path
from .views import voice_call

urlpatterns = [
   path('voice_call/<int:id>/', voice_call, name='voice_call'),
]
