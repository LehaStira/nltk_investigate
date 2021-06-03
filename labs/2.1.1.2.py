from nltk.corpus import nps_chat
from nltk import FreqDist


def main():
    chatroom = nps_chat.posts('10-19-20s_706posts.xml')
    #fdist = FreqDist(str(chatroom))
    all_chat = list(chatroom)
    result = list()
    for i in all_chat:
        for j in i:
            result.append(j)
    print(result)
    result = [i for i in result if not i.islower()]
    result = [i for i in result if i != '.' and i != ',' and i != '.' and i != '/' and i != "'" and i != '!']
    result = ' '.join(result)
    fdist = FreqDist(str(result))
    print(fdist.most_common(10))


if __name__ == '__main__':
    main()