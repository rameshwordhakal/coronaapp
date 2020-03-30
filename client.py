import requests

def send_message():
    bot_token = '1090656801:AAHFCqI-cGDFZ1oKyXBAaqx9o0ifQ2SAX1M'
    bot_chatID = ''
    message = "Hello I am from server."
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + message
    response = requests.get(send_text)

    return response.json()

message = send_message()
print("Message")
print(message)