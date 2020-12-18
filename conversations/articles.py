import csv
import pymorphy2
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
            self.message.reply_text("Что ищем?")
            return "defined"
        else:
            self.message.reply_text("Может, я могу что-то подсказать? Что интересно?")
            return "undefined"

    # поик определенной статьи
    def defined(self, context):
        msg = self.message.text
        self.message.reply_text("Ищу по имени! " + msg)
        word, flag = find_by_name(msg)
        if flag:
            self.message.reply_text("Какое странное название...")
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
            self.message.reply_text("Я пока не могу помочь с этим. Давай попробуем ещё раз?")
            return ConversationHandler.END


def find_by_name(name):
    flag = False
    morph = pymorphy2.MorphAnalyzer()
    words = name.split()
    for w in words:
        wn = morph.parse(w)[0].normal_form
        if 'NOUN' in morph.parse(w)[0].tag:
            flag = True

    with open('articles.csv', newline='', encoding="utf-8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            if row[0] in words:
                return row, flag

def find_by_book(name):
    with open('articles.csv', newline='', encoding="utf-8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:

            print(row)

def find_by_author(name):
    with open('articles.csv', newline='', encoding="utf-8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(row)


def find_by_doi(name):
    with open('articles.csv', newline='', encoding="utf-8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(row)