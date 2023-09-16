import requests

def hit_sender(card,message,chat_id):
    bot_token = '947313473:AAFvEUGCgz3zoVe4uIgLwuOopTCgrlXAdM0'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}
    requests.post(url, data=data)
