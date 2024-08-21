import telebot

tele_api_key = ''
tele_user_id = ''


def send_telegram_notification(message):
    if tele_api_key != "":
        bot = telebot.TeleBot(tele_api_key, parse_mode=None)
        bot.send_message(chat_id=tele_user_id, text=message)
    else:
        return


def send_notification(message):
    send_telegram_notification(message)
    # TODO: multiple send (discord, other)
