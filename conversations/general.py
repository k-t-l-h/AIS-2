import datetime

from telegram import ReplyKeyboardMarkup, ParseMode, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

from replics.errors import SORRY, ALL
from replics.hello import GREETINGS, JOKES
from vocabulary.general import isFindKeyword, isNo, isJoke
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

        my_keyboard = ReplyKeyboardMarkup([['Посмотреть команды', 'Поболтать']],
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
            self.message.reply_text("Являются ли команды допустимыми в диалоговых системах? "
                                    "Вот и я не знаю... Так что пока у меня нет команд. "
                                    "Что-нибудь ещё?", reply_markup=keyboard)
            return "general"
        else:
            self.message.reply_text(choice(ALL), reply_markup=keyboard)
            return "all"

    def all(self, context):
        keyboard = ReplyKeyboardRemove()
        msg = self.message.text
        # Определяемся, что делаем, смотрим, ищем или слушаем шутку
        if isJoke(msg):
            self.message.reply_text(choice(JOKES))
            self.message.reply_text("Ещё что-нибудь?")
            return "all"
        elif isArticleKeyword(msg) and isFindKeyword(msg):
            self.message.reply_text("Это что-то конкретное?")
            return "choose"
        elif isArticleKeyword(msg):
            return "article_show"
        elif isBookKeyword(msg) and isFindKeyword(msg):
            return "book"
        elif isBookKeyword(msg):
            return "book_show"
        elif isNo(msg):
            return ConversationHandler.END
        else:
            self.message.reply_text(choice(SORRY))
            return "all"

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

