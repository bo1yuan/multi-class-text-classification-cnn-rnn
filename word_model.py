import keras
from gensim.models import word2vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',level=logging.INFO)
sentences = word2vec.Text8Corpus(u"commentSettle.txt")
model = word2vec.Word2Vec(sentences, size=200, workers=15)
model.save("./model1/model")
