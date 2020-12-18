from telegram.ext import Updater, CommandHandler,RegexHandler, Filters, MessageHandler, ConversationHandler

from conversations.articles import Article
from data.data import GenerateData
from settings import API_TOKEN
from conversations.general import Handler
from conversations.books import Book


updater = Updater(API_TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start():
    # начало разговора
    # dispatcher.add_handler(CommandHandler("start", Handler.start))
    # начало
    dispatcher.add_handler(ConversationHandler(
        entry_points=[MessageHandler(Filters.all, Handler.start, pass_user_data=True)],
        states={
            "general": [MessageHandler(Filters.all, Handler.general)],
            "all": [MessageHandler(Filters.all, Handler.all)],
            "search":  [MessageHandler(Filters.all, Handler.search)],
            "choose": [MessageHandler(Filters.all, Article.defined)],
            "article": [MessageHandler(Filters.all, Article.choose)],
            "defined": [MessageHandler(Filters.all, Article.defined)],
            "undefined": [MessageHandler(Filters.all, Article.undefined)],
            "books": [MessageHandler(Filters.all, Book.start)],
        },
        fallbacks=[MessageHandler(Filters.all, Handler.all_message)]
    ))

    # если вдруг ответа не нашлось
    dispatcher.add_handler(MessageHandler(Filters.all, Handler.all_message))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    #GenerateData()
    start()
