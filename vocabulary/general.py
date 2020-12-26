import csv

import pymorphy2
from natasha import NamesExtractor, MorphVocab

from data.data import Art

FIND = {"найти", "находить", "отыскивать", "откапывать", "раздобыть",
        "узнать", "разыскать", "подобрать", "выудить", "вытащить",
        "выяснить", "определить", "установить", "поиск", "искать", "ищу", "найди"}

YES = {"да", "верно", "правильно", "отлично", "точно", "определённо", "ясно", "ага", "угу"}
NO = {"нет", "не"}

THEMES = {"о", "про", "тема"}
JOKE = {"шутка", "анекдот", "шуточка", "прикол"}


def isFindKeyword(text):
    flag = False
    text = ReplaceSyn(text)
    morph = pymorphy2.MorphAnalyzer()
    words = text.split()
    for w in words:
        wn = morph.parse(w)[0].normal_form
        if wn in FIND:
            flag = True
    return flag


def isYes(text):
    flag = False
    text = ReplaceSyn(text)
    morph = pymorphy2.MorphAnalyzer()
    words = text.split()
    for w in words:
        wn = morph.parse(w)[0].normal_form
        if wn in YES:
            flag = True
    return flag


def isNo(text):
    flag = False
    text = ReplaceSyn(text)
    morph = pymorphy2.MorphAnalyzer()
    words = text.split()
    for w in words:
        wn = morph.parse(w)[0].normal_form
        if wn in NO:
            flag = True
    return flag


def isName(text):
    flag = False
    text = ReplaceSyn(text)
    morph_vocab = MorphVocab()
    extractor = NamesExtractor(morph_vocab)
    matches = extractor(text)
    facts = [_.fact.as_json for _ in matches]
    if len(facts) != 0:
        flag = True
    return flag


def NameExtract(text):
    text = ReplaceSyn(text)
    morph_vocab = MorphVocab()
    extractor = NamesExtractor(morph_vocab)
    matches = extractor(text)
    name = []
    facts = [_.fact.as_json for _ in matches]
    for key, value in facts[0].items():
        name.append(value)
    return name


def isThemeKeyword(text):
    flag = False
    text = ReplaceSyn(text)
    morph = pymorphy2.MorphAnalyzer()
    words = text.split()
    for w in words:
        wn = morph.parse(w)[0].normal_form
        if wn in THEMES:
            flag = True
    return flag


def isJoke(text):
    flag = False
    text = ReplaceSyn(text)
    morph = pymorphy2.MorphAnalyzer()
    words = text.split()

    for w in words:

        wn = morph.parse(w)[0].normal_form
        if wn in JOKE:
            flag = True
    return flag


def ReplaceSyn(text):
    text = text.replace("?", "")
    text = text.replace(".", "")
    text = text.replace(",", "")
    text = text.replace(":", "")
    text = text.replace("!", "")
    return text


def LoadData():
    alls = []
    with open('articles.csv', newline='', encoding="utf-8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

        for row in spamreader:
            a = Art("")
            a.name = row[0]
            a.field = row[1]
            a.book = row[2]
            a.doi = row[3]
            a.author = row[4]
            a.score = row[5]
            alls.append(a)
    return alls
