#coding=utf-8

from gensim.models import word2vec
import logging
import json
import codecs


logging.basicConfig(format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',level=logging.INFO)

def most_similar(word):
    model = word2vec.Word2Vec.load('model')
    print model[u'位置'][:10]

    tags = model.most_similar(word, topn=30)
    res = []
    for item in tags:
        res.append(item[0])
    return res

def most_similars(words):
    ress = {}
    for word in words:
        res = most_similar(word)
        ress[word] = res
    return ress


if __name__ == '__main__':
    words = [u'位置',u'满意',u'推荐',u'性价比',u'服务态度',u'卫生',u'隔音',u'门锁',u'Wifi']
    #ress = most_similars(words)
    most_similar(u'满意')
    """ with codecs.open('./data/most_similars.json','w',encoding='utf-8') as f:
        json.dump(ress, f, ensure_ascii=False)
        f.write('\n')
    """
