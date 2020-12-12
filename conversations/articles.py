from telegram.ext import ConversationHandler


class Article:
    def __init__(self):
        self.message = None
        self.effective_chat = None

    # начало поиска статьи
    def start(self, context):
        self.message.reply_text("мяу")
        return "defined"

    # параметры
    def choose(self, context):
        msg = self.message.text
        if msg == "Да":
            self.message.reply_text("мяу")
            return "defined"
        else:
            self.message.reply_text("мяу")
            return "undefined"

    # поик определенной статьи
    def defined(self, context):
        self.message.reply_text("мяу 2")
        return "undefined"

    # поик неопределенной статьи
    def undefined(self, context):
        self.message.reply_text("мяу 3")
        return ConversationHandler.END
