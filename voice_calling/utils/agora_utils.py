# utils/agora_utils.py

import requests

def generate_agora_token(app_id, app_certificate, channel_name, user_id, expiration_time_in_seconds=3600):
    url = f'https://api.agora.io/v1/token?appId={app_id}&appCertificate={app_certificate}&channelName={channel_name}&userId={user_id}&role=PUBLISHER&expire={expiration_time_in_seconds}'
    
    response = requests.post(url)
    token = response.json().get('rtcToken')
    return token
