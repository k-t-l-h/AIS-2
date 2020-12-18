import pymorphy2
from natasha import NamesExtractor,  MorphVocab

FIND = {"найти", "находить", "отыскивать", "откапывать", "раздобыть",
        "узнать", "разыскать", "подобрать", "выудить", "вытащить",
        "выяснить", "определить", "установить", "поиск"}

YES = {"да", "верно", "правильно", "отлично", "точно", "определённо", "ясно", "ага", "угу"}
NO = {"нет"}

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