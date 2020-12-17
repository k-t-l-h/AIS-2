from vocabulary.general import isYes, isNo, isName, isThemeKeyword
from telegram.ext import ConversationHandler
from vocabulary.book import isBase

class Book:
    def __init__(self):
        pass

    def start(self, context):
        self.message.reply_text("Что интересно?")
        return "book_choose"

    # параметры
    def choose(self, context):
        msg = self.message.text
        if isThemeKeyword(msg):
            self.message.reply_text("Журнал по теме")
            return ConversationHandler.END
        elif isBase(msg):
            self.message.reply_text("Журнал по типу")
            return ConversationHandler.END
        elif isName(msg):
            self.message.reply_text("Журнал по названию")
            return ConversationHandler.END
        else:
            self.message.reply_text("Что интересно?")
            return ConversationHandler.END
