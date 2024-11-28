import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download NLTK resources
nltk.download('wordnet')
nltk.download('stopwords')

def preprocess_text(sentences, stopwords=None):
    if stopwords is None:
        stopwords = []
    ps = PorterStemmer()
    lm = WordNetLemmatizer()

    processed = [
        [lm.lemmatize(ps.stem(word.lower())) for word in sentence if word.lower() not in stopwords]
        for sentence in sentences
    ]
    return processed

def sentence_similarity(sent1, sent2, stopwords=None):
    stopwords = stopwords or []
    all_words = list(set(sent1 + sent2))
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    for word in sent1:
        vector1[all_words.index(word)] += 1
    for word in sent2:
        vector2[all_words.index(word)] += 1

    return 1 - cosine_distance(vector1, vector2)

def build_similarity_matrix(sentences, stop_words):
    n = len(sentences)
    matrix = np.zeros((n, n))

    for idx1 in range(n):
        for idx2 in range(n):
            if idx1 != idx2:
                matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)
    return matrix
