# views.py

from django.shortcuts import render
from .utils.agora_utils import generate_agora_token

# def voice_call(request):
#     app_id = "3fa01637b98c4d15a411e3baa9f219e6"
#     app_certificate = "6d2efd87ac6d47058adffa5e3177a295"
#     user_id = request.user.agora_user_id
#     channel_name = "JyotishJunction"

#     agora_token = generate_agora_token(app_id, app_certificate, channel_name, user_id)

#     return render(request, 'voice_calling/voice_call.html', {'agora_token': agora_token})

def voice_call(request, call_id):
    app_id = "3fa01637b98c4d15a411e3baa9f219e6"
    app_certificate = "6d2efd87ac6d47058adffa5e3177a295"
    user_id = request.user.agora_user_id
    channel_name = "JyotishJunction"

    agora_token = generate_agora_token(app_id, app_certificate, channel_name, user_id)
    return render(request, 'voice_calling/voice_call.html', {'call_id': call_id ,'agora_token':agora_token})



