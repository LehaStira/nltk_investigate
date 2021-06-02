from nltk.book import *


def five_prints():
    print()
    print()
    print()
    print()
    print()


def main():
    print(f'text1 is {text1}')
    five_prints()
    print('Context of word "monstrous" is: ')
    text1.concordance('monstrous')  # контекст слова
    five_prints()
    print('Words, similar to monstrous is: ')
    text1.similar('monstrous')  # какие слова еще содержатся в подобном контексте?
    five_prints()
    print('Common context to words "monstrous" and "very" is: ')
    text2.common_contexts(['monstrous', 'very'])  # общие контексты для нескольких слов из одного текста
    five_prints()
    list_of_words = ['citizen', 'democracy', 'freedom', 'duties', 'America']
    text4.dispersion_plot(list_of_words)  # график как часто встречается то или иное слово
    text5.generate()  # генерим текст, который похож не текст



if __name__ == '__main__':
    main()