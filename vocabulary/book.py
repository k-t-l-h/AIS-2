import pymorphy2

BOOK = {"журнал", "издание", "альманах", "сборник", "выпуск", "учебник"}
BASE = {"РИНЦ", "ВАК", "WoS"}


def isBookKeyword(text):
    flag = False

    morph = pymorphy2.MorphAnalyzer()
    words = text.split()
    for w in words:
        wn = morph.parse(w)[0].normal_form
        if wn in BOOK:
            flag = True
    return flag

def isBase(text):
    flag = False

    morph = pymorphy2.MorphAnalyzer()
    words = text.split()
    for w in words:
        wn = morph.parse(w)[0].normal_form
        if wn in BASE:
            flag = True
    return flag
