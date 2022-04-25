import math

from nltk import sent_tokenize, word_tokenize, PorterStemmer
from nltk.corpus import stopwords
import nltk
import pickle as cPickle

nltk.download('stopwords')
nltk.download('punkt')


def decision(data):
    return 1


def pickle_file(pf):
    with open(pf, 'rb') as pickle_file:
        tweets = cPickle.load(pickle_file)
    data = {}
    data['datetime'] = []
    data['body'] = []
    index = 0
    for tweet in tweets:
        print(index)
        data['datetime'].append(tweet._json['created_at'])
        data['body'].append(tweet._json['text'])
        index += 1
    return decision(data['datetime'])


def frequency_table(full):
    frequency_matrix = {}
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    for sent in full:
        frequency_table = {}
        words = word_tokenize(sent)
        for word in words:
            word = word.lower()
            word = ps.stem(word)
            if word in stop_words:
                continue
            if word in frequency_table:
                frequency_table[word] += 1
            else:
                frequency_table[word] = 1
        frequency_matrix[sent[15:]] = frequency_table
    return frequency_matrix


def tfMatrix(frequency_matrix):
    matrix = {}
    for tweet, frequency_table in frequency_matrix.items():
        tf_table = {}
        word_count = len(frequency_table)
        for word, count in frequency_table.items():
            tf_table[word] = count / word_count
        matrix[tweet] = tf_table
    return matrix


def tweets_per_word(frequency_matrix):
    word_per_table = {}

    for tweet, frequency_table in frequency_matrix.items():
        for word, count in frequency_table.items():
            if word in word_per_table:
                word_per_table[word] += 1
            else:
                word_per_table[word] = 1
    return word_per_table


def idf_matrix(frequency_matrix, tweets_per_word, total_documents):
    matrix = {}

    for tweet, frequency_table in frequency_matrix.items():
        table = {}
        for word in frequency_table.keys():
            table[word] = math.log10(total_documents / float(tweets_per_word[word]))
        matrix[tweet] = table
    return matrix


def create_tfidf(tf, idf):
    tfidf = {}
    for (tweet1, table1), (tweet2, table2) in zip(tf.items(), idf.items()):
        temp_table = {}

        for (word1, val1), (word2, val2) in zip(table1.items(), table2.items()):
            tfidf[word1] = float(val1) * float(val2)
        tfidf[tweet1] = temp_table

    return tfidf

def scores(tfidf):
    vals={}
    for tweet,table in tfidf.items():
        tot = 0
        for word, score in table.items():
            tot +=score
        vals[tweet] = tot/len(table)
    return vals


def create_summary(tweets,vals,avg_score):
    str = ''
    i = 0
    for tweet in tweets:
        if tweets[:15] in vals and vals[tweet[:15]] >=avg_score:
            str += " " + tweet
            i+=1
    return str


def avg_score(vals):
    tot = 0
    for i in vals:
        tot += vals[i]
    avg = tot / len(vals)
    return avg


def summary(tweets):
    frequencyTable = frequency_table(tweets)
    tf = tfMatrix(frequencyTable)
    per_word = tweets_per_word(frequencyTable)
    idf = idf_matrix(frequencyTable, per_word, len(tweets))
    tfidf = create_tfidf(tf, idf)
    vals = scores(tfidf)
    return create_summary(tweets,vals,3.5*avg_score(vals))

