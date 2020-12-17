import datetime

from telegram import ReplyKeyboardMarkup, ParseMode, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

from replics.errors import SORRY
from replics.hello import GREETINGS, description
from vocabulary.general import isFindKeyword, isNo
from vocabulary.article import isArticleKeyword
from vocabulary.book import isBookKeyword
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

        my_keyboard = ReplyKeyboardMarkup([['Посмотреть команды', 'Поиск', 'Справочник']],
                                          resize_keyboard=True, ReplyKeyboardRemove=True)
        self.message.reply_text(text.format(chat.first_name), reply_markup=my_keyboard,
                                parse_mode=ParseMode.MARKDOWN)
        return "general"

    def general(self, context):
        keyboard = ReplyKeyboardRemove()
        msg = self.message.text
        if msg == 'Посмотреть команды':
            keyboard = ReplyKeyboardMarkup([['Поиск']],
                                           resize_keyboard=True)
            self.message.reply_text("Извини, пока у меня нет команд :). "
                                    "Что-нибудь ещё?", reply_markup=keyboard)
            return "general"
        elif isFindKeyword(msg):
            self.message.reply_text("Хорошо, что мы сегодня ищем?", reply_markup=keyboard)
            return "search"
        else:
            keyboard = ReplyKeyboardMarkup([['Искать']],
                                           resize_keyboard=True)
            self.message.reply_text(choice(SORRY), reply_markup=keyboard)
            return "general"

    def search(self, context):
        msg = self.message.text
        if isArticleKeyword(msg):
            self.message.reply_text("Хорошо! Будем искать статью. Это конкретная статья?")
            return "article"
        elif isBookKeyword(msg):
            self.message.reply_text("Хорошо! Будем искать журнал. Это конкретный журнал?")
            return "book"
        else:
            self.message.reply_text(choice(SORRY))
            return "search"

    def all_message(self, context):
        keyboard = ReplyKeyboardRemove()
        msg = self.message.text
        if isNo(msg):
            return ConversationHandler.END
        self.message.reply_text(choice(SORRY), reply_markup=keyboard)

