from nltk.corpus import brown
from pprint import pprint
"""
Используя справочную систему, перечислите и опишите возможности корпуса Брауна, которые не упоминались ранее в тексте.
Ответ:
в корпусе брауна так же есть предложения (57340 предложений)
Их тоже можно делить по категориям
"""


def main():
    brown_categories = brown.categories()
    pprint(brown_categories)
    words = brown.words(categories = 'news')
    a = brown.sents(categories = 'news')
    print(len(a))
    #for i in a:
     #   print(i)


if __name__ == '__main__':
    main()