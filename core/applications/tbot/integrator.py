import json

import requests

from project import settings


class TelegramBotIntegration:
    url = f'https://api.telegram.org/bot{settings.BOT_API_KEY}'
    chat_id = settings.BOT_CHAT_ID

    def send_message(self, text, event_type, event_id):
        url = f'{self.url}/sendMessage'
        keyboard = [
            [
                {'text': 'Принять', 'callback_data': f'{event_type}.{event_id}'},
            ]
        ]

        buttons = {'inline_keyboard': keyboard}
        json_data = json.dumps(buttons)
        data = {'text': text, 'chat_id': settings.BOT_CHAT_ID, 'reply_markup': json_data, 'parse_mode': 'markdown'}

        response = requests.post(url, data=data)
        if response:
            return response.json()
