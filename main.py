from nltk.book import *
from nltk import FreqDist

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

    five_prints()

    print(f'len of all text3 is {len(text3)}')
    print(f'len of unique words in text3 is {len(set(text3))}')

    five_prints()

    print(f'lexical richness  (lexical diversity) of text3 is {len(set(text3)) / len(text3)}')  # лексическое богатстсво текста

    five_prints()

    print(f'Count of word "smote" in text3 is {text3.count("smote")}')
    print(f'percent of word "smote" in this text is {100*text3.count("smote")/ len(text3)}')

    fdist = FreqDist(text1)  # частнотное распределение - количество слов в предложении
    print(f'fdist of first text is {fdist.most_common(10)}')  # в качестве параметра - количество самых распространенных слов

    five_prints()

    print(fdist.hapaxes())  # слова, которые встречаются в тексте всего один раз

    five_prints()

    fdist.plot(59, cumulative = True)  # 59 самых встречающихся слов на графике

    print('Words in text len of that are more then 19')
    my_text = set(text1)
    long_words = [w for w in my_text if len(w)>19]
    print(long_words)

    five_prints()

    print('Words in text len of that are more that 10 and frequency distribution more 5')

    fdist5 = FreqDist(text5)
    my_text5 = set(text5)
    res = [i for i in my_text5 if len(i) > 10 and fdist5[i] > 5]
    print(sorted(res))

    five_prints()

    # collocation - словосочетание
    print('Here is bigrams')  # биграммы это просто пары слов
    print(list(bigrams(['more', 'hello', 'good bye']))) # output is [('more', 'hello'), ('hello', 'good bye')]

    five_prints()

    print('Here is collocations: ') # выведем словосочитания из текста 1
    text1.collocations()

    five_prints()

    # мы можем посчитать freqdist от количества букв в словах

    print('Here is frequency distribution of len of words: ')
    my_fdist = FreqDist(len(i) for i in text1)
    print(my_fdist.most_common())  # формат (длина (или другая искомая величина), количество) [(3, 50223), (1, 47933), (4, 42345), (2, 38513)

    five_prints()

    print(f'Maximum count of words is words with len: {my_fdist.max()}')

    five_prints()

    print(my_fdist.freq(5))  # процент слов с длиной 5


if __name__ == '__main__':
    main()