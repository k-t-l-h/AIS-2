from telegram.ext import Updater, CommandHandler,RegexHandler, Filters, MessageHandler, ConversationHandler

from conversations.articles import Article
from settings import API_TOKEN
from conversations.general import Handler


updater = Updater(API_TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start():
    # начало разговора
    dispatcher.add_handler(CommandHandler("start", Handler.start))
    dispatcher.add_handler(ConversationHandler(
        entry_points=[RegexHandler('^Перейти к поиску', Article.start, pass_user_data=True)],
        states={
            "defined": [MessageHandler(Filters.all, Article.defined)],
            "undefined": [MessageHandler(Filters.all, Article.undefined)],
        },
        fallbacks=[MessageHandler(Filters.all, Handler.all_message)]
    ))
    # если вдруг ответа не нашлось
    dispatcher.add_handler(MessageHandler(Filters.all, Handler.all_message))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    start()
