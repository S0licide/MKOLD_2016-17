import re, os, json


def openf():
    files = os.listdir('udm')
    for f in files:
        way = 'udm/' + f
        file = open(way, 'r', encoding='utf-8')
        words = file.read()
        reg(words)

def reg(words):
    regex = '-lexeme\\n lex: (.*?)\\n .*? gramm: (.*?)\\n .*? trans_ru: (.*?)\\n'
    res = re.findall(regex, words, flags=re.DOTALL)
    if res:
        d = {}
        for elem in res:
            a = []
            a.append(elem[1])
            a.append(elem[2])
            a = tuple(a)
            d[elem[0]] = a
        print(d)
        filejson = open('data.json', 'a', encoding='utf-8')
        json.dump(d, filejson)
        filejson.close()


openf()