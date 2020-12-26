import csv
import time
from random import random

from faker import Faker


class Art:
    name = ""
    field = ""
    book = ""
    doi = ""
    author = ""
    score = 0.0

    def __init__(self):
        fake = Faker("ru_RU")
        Faker.seed(time.time())
        self.name = fake.word()
        self.field = fake.word(ext_word_list=['математика', 'информатика', 'прочее'])
        self.book = fake.bs()
        self.doi = "10.100" + "/" + str(fake.credit_card_security_code())
        self.author = fake.name_nonbinary()
        self.score = random()

    def __init__(self, a):
        fake = Faker("ru_RU")
        Faker.seed(time.time())
        self.name = fake.word()
        self.field = fake.word(ext_word_list=['математика', 'информатика', 'прочее'])
        self.book = fake.bs()
        self.doi = "10.100" + "/" + str(fake.credit_card_security_code())
        self.author = fake.name_nonbinary()
        self.score = random()


def GenerateData():
    with open('articles.csv', 'w', newline='', encoding="utf-8") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(0, 100):
            ar = Art()
            spamwriter.writerow([ar.name, ar.field, ar.book, ar.doi, ar.author, ar.score])
