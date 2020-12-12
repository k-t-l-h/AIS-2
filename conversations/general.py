import datetime

from telegram import ReplyKeyboardMarkup, ParseMode

from replics.errors import SORRY
from replics.hello import GREETINGS, description
from random import choice


class Handler:
    return_flag = True

    def __init__(self):
        self.message = None
        self.effective_chat = None

    def start(self, context):
        chat = self.effective_chat
        now = datetime.datetime.now().hour
        # красиво здороваемся
        if now < 6:
            text = GREETINGS[0]
        elif now < 12:
            text = GREETINGS[1]
        elif now < 18:
            text = GREETINGS[2]
        else:
            text = GREETINGS[3]

        my_keyboard = ReplyKeyboardMarkup([['Посмотреть команды', 'Перейти к поиску']],
                                          resize_keyboard=True)
        self.message.reply_text(text.format(chat.first_name), reply_markup=my_keyboard,
                                parse_mode=ParseMode.MARKDOWN)

    def mp(self, context):
        my_keyboard = ReplyKeyboardMarkup([['/start', '/commands']])
        self.message.reply_text("Тыки кнопку!", reply_markup=my_keyboard, parse_mode=ParseMode.MARKDOWN)

    def getInfo(self, context):
        pass

    def all_message(self, context):
        msg = self.message.text
        print(msg)
        if msg == 'Посмотреть команды':
            self.message.reply_text(description)
        elif msg == 'Перейти к поиску':
            self.message.reply_text("Хорошо, что мы сегодня ищем?")
        else:
            self.message.reply_text(choice(SORRY))
