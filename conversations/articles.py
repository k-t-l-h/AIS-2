from telegram.ext import ConversationHandler
from vocabulary.general import isYes, isNo, isName, isThemeKeyword
from vocabulary.article import isBookKeyword, isDOIKeyword


class Article:
    def __init__(self):
        self.message = None
        self.effective_chat = None

    # параметры
    def choose(self, context):
        msg = self.message.text
        if isYes(msg):
            self.message.reply_text("Что за статья?")
            return "defined"
        else:
            self.message.reply_text("Что интересно?")
            return "undefined"

    # поик определенной статьи
    def defined(self, context):
        msg = self.message.text
        self.message.reply_text("Ищем статью " + msg)
        if isDOIKeyword(msg):
            self.message.reply_text("Ищу статью по doi")
        self.message.reply_text("Спасибо, что потестировали меня!")
        return ConversationHandler.END

    # поик неопределенной статьи
    def undefined(self, context):
        msg = self.message.text
        if isBookKeyword(msg):
            self.message.reply_text("Ищу статью в журнале")
            return ConversationHandler.END
        elif isDOIKeyword(msg):
            self.message.reply_text("Ищу статью по doi")
            return ConversationHandler.END
        elif isThemeKeyword(msg):
            self.message.reply_text("Ищу статью по теме")
            return ConversationHandler.END
        elif isName(msg):
            self.message.reply_text("Ищу статью по автору")
            return ConversationHandler.END
        else:
            self.message.reply_text("Определитесь и возвращайтесь. Спасибо!")
            return ConversationHandler.END
