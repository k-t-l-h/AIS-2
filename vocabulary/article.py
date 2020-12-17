import pymorphy2
from yargy.predicates import gte, lte
from yargy import and_, rule, Parser

ARTICLE = {"статья", "публикация", "книга", "работа",
           "труд", "произведение", "отчёт", "доклад", "выработка", "диссертация"}


BOOK = {"из", "в", "журнал", "издание", "альманах", "сборник", "выпуск", "учебник"}

NUMBER = rule(
    gte(0)
)

DOI_RULE = rule(NUMBER, ".", NUMBER, "/", NUMBER)


def isArticleKeyword(text):
    flag = False

    morph = pymorphy2.MorphAnalyzer()
    words = text.split()
    for w in words:
        wn = morph.parse(w)[0].normal_form
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
