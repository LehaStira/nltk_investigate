"""
Неоднозначность смысла слов
Turn right at the next street
I’m on the right
I’m always right
ИЛИ
Their house was damaged by the fire
He was fired on the last week
"""
from nltk.corpus import brown
from pprint import pprint


def main():
    brown_categories = brown.categories()
    pprint(brown_categories)
    words = brown.words(categories = 'news')
    for word in words:
        print(word)


if __name__ == '__main__':
    main()