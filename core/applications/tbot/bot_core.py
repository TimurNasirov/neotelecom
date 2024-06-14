from datetime import datetime, timedelta
from telebot import TeleBot, types
from calendar import monthrange
from pytz import utc

from applications.core.models import JoinUs, CallMe
from project import settings

t_bot = TeleBot(settings.BOT_API_KEY)


def _get_users_list(obj):
    users = {}
    for item in obj:
        if item.user in users.keys():
            users[item.user] += 1
            continue
        users[item.user] = 1

    join_us_users = ''
    for user in users:
        join_us_users += f" \n{user}  \\-  {users[user] }"

    return join_us_users


@t_bot.message_handler(commands=["statistic"])
def repeat_all_messages(message):
    first_day = datetime.now().replace(day=1, tzinfo=utc)
    current_time = datetime.now().replace(tzinfo=utc)

    join_us = JoinUs.objects.filter(status='accepted', created_at__gte=first_day, created_at__lte=current_time).all()
    join_us_users = _get_users_list(join_us)

    call_me = CallMe.objects.filter(status='accepted', created_at__gte=first_day, created_at__lte=current_time).all()
    call_me_users = _get_users_list(call_me)

    markup = types.InlineKeyboardMarkup()
    start_time = current_time.strftime("%Y-%m")
    markup.add(
        types.InlineKeyboardButton('Предыдущий месяц', callback_data=f'repeat.{current_time - timedelta(days=monthrange(int(current_time.strftime("%Y")), int(current_time.strftime("%m")))[1])}')
    )

    text = (f'*Статистика по операторам за текущий месяц* \n'
            f'Принято заявок на подключение: {join_us_users if join_us_users else "0"} \n'
            f'\n\n'
            f'Принято обратных звонков: {call_me_users if call_me_users else "0"} \n'
            )

    t_bot.send_message(message.chat.id, text, parse_mode='markdownV2', reply_markup=markup)


@t_bot.callback_query_handler(func=lambda call: True)
def get_callback_user(call):
    if call:
        message = call.message
        user = call.from_user
        
        if user.username:
            user_data = f'@{user.username}'
        elif user.last_name and user.first_name:
            user_data = f'{user.last_name} {user.first_name}'
        elif user.last_name:
            user_data = user.last_name
        else:
            user_data = user.first_name

        data = call.data.split('.')
        if data[0] == 'join_us':
            join_us = JoinUs.objects.filter(pk=data[1]).last()
            if not join_us:
                t_bot.send_message(message.chat.id, 'Произошла какая-то ошибка. Не могу найти заявку :(')
                return

            if join_us.status == 'accepted':
                t_bot.send_message(message.chat.id, 'Заявка уже обработна другим оператором.')
                return

            join_us.status = 'accepted'
            join_us.user = user_data
            join_us.save()

            t_bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                                text=f'{message.text}\nЗаявку принял(а) {user_data}',
                                reply_markup=None)

        elif data[0] == 'call_me':
            call_me = CallMe.objects.filter(pk=data[1]).last()
            if not call_me:
                t_bot.send_message(message.chat.id, 'Произошла какая-то ошибка. Не могу найти заявку :(')
                return

            if call_me.status == 'accepted':
                t_bot.send_message(message.chat.id, 'Заявка уже обработна другим оператором.')
                return

            call_me.status = 'accepted'
            call_me.user = user_data
            call_me.save()

            t_bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                                text=f'{message.text}\nЗаявку принял(а) {user_data}',
                                reply_markup=None)

        elif data[0] == 'repeat':
            if current_time.strftime('%Y') == '1969':
                t_bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
                t_bot.send_message(chat_id=message.chat.id, message_id=message.message_id, text='Ошибка. Слишком маленький год')
            else:
                data[1] = datetime.fromisoformat(data[1]).replace(tzinfo=utc)
                first_day = data[1].replace(day=1)
                current_time = data[1].replace(day=monthrange(int(data[1].strftime('%Y')), int(data[1].strftime('%m')))[1])

                join_us = JoinUs.objects.filter(status='accepted', created_at__gte=first_day, created_at__lte=current_time).all()
                join_us_users = _get_users_list(join_us)

                call_me = CallMe.objects.filter(status='accepted', created_at__gte=first_day, created_at__lte=current_time).all()
                call_me_users = _get_users_list(call_me)
                
                markup = types.InlineKeyboardMarkup(row_width=2) 
                if datetime.now().strftime('%Y-%m') != current_time.strftime('%Y-%m'):    
                    try:
                        previous = current_time.replace(day=monthrange(int(current_time.strftime("%Y")), int(current_time.strftime("%m")) - 1)[1], month=int(current_time.strftime("%m")) - 1)
                    except ValueError:
                        previous = current_time.replace(day=31, year=int(current_time.strftime("%Y")) - 1, month=12 if current_time.strftime('%m') != '12' else 1)
                    try:
                        _next = current_time.replace(day=monthrange(int(current_time.strftime("%Y")), int(current_time.strftime("%m")) + 1)[1], month=int(current_time.strftime("%m")) + 1)
                    except ValueError:
                        _next = current_time.replace(day=31, year=int(current_time.strftime("%Y")) + 1, month=12 if current_time.strftime('%m') != '12' else 1)
                    markup.row(
                        types.InlineKeyboardButton('Предыдущий месяц', callback_data=f'repeat.{previous}'),
                        types.InlineKeyboardButton('Следующий месяц', callback_data=f'repeat.{_next}')
                    )
                else:
                    markup.row(
                        types.InlineKeyboardButton('Предыдущий месяц', callback_data=f'repeat.{current_time - timedelta(days=monthrange(int(current_time.strftime("%Y")), int(current_time.strftime("%m")))[1])}')
                    )

                text = (f'*Статистика по операторам за {current_time.strftime("%m\\.%Y")}* \n'
                        f'Принято заявок на подключение: {join_us_users if join_us_users else "0"} \n'
                        f'\n\n'
                        f'Принято обратных звонков: {call_me_users if call_me_users else "0"} \n'
                        )
                
                t_bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=text, parse_mode='markdownV2', reply_markup=markup)