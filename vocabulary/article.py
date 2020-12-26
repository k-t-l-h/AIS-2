import pymorphy2
from yargy.predicates import gte, lte
from yargy import and_, rule, Parser

ARTICLE = {"статья", "публикация", "книга", "работа",
           "труд", "произведение", "отчёт", "доклад", "выработка", "диссертация"}

BOOK = {"из", "в", "журнал", "книга", "издание", "альманах", "сборник", "выпуск", "учебник"}

BEST = {"лучший", "хороший", "превосходный", "профессиональный", "замечательный", "выдающийся", "достойный"}
NEWEST = {"новый", "последний", "недавний", "крайний", "свежий"}
NUMBER = rule(
    gte(0)
)

DOI_RULE = rule(NUMBER, ".", NUMBER, "/", NUMBER)


def isBest(text):
    flag = False

    morph = pymorphy2.MorphAnalyzer()
    words = text.split()
    for w in words:
        wn = morph.parse(w)[0].normal_form
        if wn in BEST:
            flag = True
    return flag


def isNewest(text):
    flag = False

    morph = pymorphy2.MorphAnalyzer()
    words = text.split()
    for w in words:
        wn = morph.parse(w)[0].normal_form
        if wn in NEWEST:
            flag = True
    return flag


def isArticleKeyword(text):
    flag = False

    morph = pymorphy2.MorphAnalyzer()
    words = text.split()
    for w in words:
        wn = morph.parse(w)[0].normal_form
        print(wn)
        if wn in ARTICLE:
            flag = True
    return flag


def isBookKeyword(text):
    flag = False

    morph = pymorphy2.MorphAnalyzer()
    words = text.split()
    for w in words:
        wn = morph.parse(w)[0].normal_form
        if wn in BOOK:
            flag = True
    return flag


def isDOIKeyword(text):
    flag = False
    parser = Parser(DOI_RULE)
    for match in parser.findall(text):
        print(match.tokens)
        return True
    return flag


def DOI(text):
    parser = Parser(DOI_RULE)
    for match in parser.findall(text):
        s = ""
        for m in match.tokens:
            s += str(m.value)
        break
    return s
