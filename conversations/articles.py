import pymorphy2
from telegram.ext import ConversationHandler

from vocabulary.article import isBookKeyword, isDOIKeyword, DOI, isBest, isNewest
from vocabulary.general import isYes, isName, isThemeKeyword, LoadData, NameExtract
from replics import hello
from random import choice

class Article:
    def __init__(self):
        self.message = None
        self.effective_chat = None

        # параметры

    def find(self, context):
        msg = self.message.text

        if isBest(msg):
            word = find_best(msg)
            self.message.reply_text(choice(hello.FINDED))
            self.message.reply_text(
                "Название: {},\nЖурнал: {},\nРейтинг: {}" +
                "\nАвторы {},\nПоле: {},\nDOI: {}".format(word.name, word.book, word.score,
                                                          word.author, word.field, word.doi)
            )

        elif isNewest(msg):
            word = find_newest(msg)
            self.message.reply_text(choice(hello.FINDED))
            self.message.reply_text(
                "Название: {},\nЖурнал: {},\nРейтинг: {}" +
                "\nАвторы {},\nПоле: {},\nDOI: {}".format(word.name, word.book, word.score,
                                                          word.author, word.field, word.doi)
            )
        return ConversationHandler.END

    # параметры
    def choose(self, context):
        msg = self.message.text
        if isYes(msg):
            self.message.reply_text("Что ищем?")
            return "defined"
        else:
            self.message.reply_text("Может, я могу что-то подсказать? Что интересно?")
            return "undefined"

    # поик определенной статьи
    def defined(self, context):
        msg = self.message.text
        if isDOIKeyword(msg):
            self.message.reply_text("Ищу статью по doi")
            doi = DOI(msg)
            word = find_by_doi(doi)
            if word is None:
                self.message.reply_text(choice(hello.UNFINDED))
                return ConversationHandler.END
            else:
                print(word.doi)
                self.message.reply_text(choice(hello.FINDED))
                self.message.reply_text(
                    "Название: {},\nЖурнал: {},\nРейтинг: {}" +
                    "\nАвторы {},\nПоле: {},\nDOI: {}".format(word.name, word.book, word.score,
                                                              word.author, word.field, word.doi)
                )
                return ConversationHandler.END

        self.message.reply_text("Ищу по названию! ")

        word, flag = find_by_name(msg)
        if flag:
            self.message.reply_text("Какое странное название...")

        if word is None:
            self.message.reply_text(choice(hello.UNFINDED))
            return ConversationHandler.END
        else:
            self.message.reply_text(choice(hello.FINDED))
            self.message.reply_text(
                "Название: {},\nЖурнал: {},\nРейтинг: {}" +
                "\nАвторы {},\nПоле: {},\nDOI: {}".format(word.name, word.book, word.score,
                                                          word.author, word.field, word.doi)
            )
            return ConversationHandler.END

    # поик неопределенной статьи
    def undefined(self, context):
        msg = self.message.text
        if isBookKeyword(msg):
            self.message.reply_text("Ищу статью по журналу")
            word = find_by_book(msg)
            if word is None:
                self.message.reply_text(choice(hello.UNFINDED))
                return ConversationHandler.END
            else:
                self.message.reply_text(choice(hello.FINDED))
                self.message.reply_text(
                    "Название: {},\nЖурнал: {},\nРейтинг: {}" +
                    "\nАвторы {},\nПоле: {},\nDOI: {}".format(word.name, word.book, word.score,
                                                              word.author, word.field, word.doi)
                )
                return ConversationHandler.END
        elif isThemeKeyword(msg):
            self.message.reply_text("Ищу статью по теме")
            return ConversationHandler.END
        elif isName(msg):
            self.message.reply_text("Ищу статью по автору")
            word = find_by_author(msg)
            if word is None:
                self.message.reply_text(choice(hello.UNFINDED))
                return ConversationHandler.END
            else:
                self.message.reply_text(choice(hello.FINDED))
                self.message.reply_text(
                    "Название: {},\nЖурнал: {},\nРейтинг: {}" +
                    "\nАвторы {},\nПоле: {},\nDOI: {}".format(word.name, word.book, word.score,
                                                              word.author, word.field, word.doi)
                )
                return ConversationHandler.END
        else:
            self.message.reply_text("Я пока не могу помочь с этим. Я научусь и мы продолжим")
            return ConversationHandler.END


def find_by_name(name):
    name = NameExtract(name)
    data = LoadData()
    for d in data:
        if d.author == name:
            return d
    return None


def find_by_doi(name):
    t = DOI(name)
    data = LoadData()

    for d in data:
        if d.doi == t:
            return d
    return None


def find_by_book(name):
    morph = pymorphy2.MorphAnalyzer()
    words = name.split()
    words2 = []
    for w in words:
        w2 = morph.parse(w)[0].normal_form
        w2 = str(w2)
        w2 = w2.lower()
        words2.append(w2)
    data = LoadData()
    for d in data:
        words = d.book
        words = str(words).lower()
        words = words.split()
        for w in words:
            if any(morph.parse(w)[0].normal_form in w2 for w2 in words2):
                return d
    return None


def find_by_author(name):
    names = NameExtract(name)
    data = LoadData()
    for d in data:
        words = d.author
        words2 = NameExtract(words)
        for w in words2:
            if any(w == name for name in names):
                return d


def find_newest(name):
    alls = LoadData()
    b = alls[0]
    for a in alls:
        if a.doi < b.doi:
            b = a
    return b


def find_best(name):
    alls = LoadData()
    b = alls[0]
    for a in alls:
        if a.score > b.score:
            b = a
    return b
