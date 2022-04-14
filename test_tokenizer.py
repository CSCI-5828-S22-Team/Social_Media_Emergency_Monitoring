import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer, PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer, ENGLISH_STOP_WORDS, TfidfVectorizer
import seaborn as sns
from datetime import datetime
import spacy
import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_first(self):
        ret=[]
        nlp = spacy.load("en_core_web_sm")
        l=nlp("hello, this is a test")
        for token in l:
            ret.append(token.text)
        self.assertEqual(ret, ['hello', ',', 'this', 'is', 'a', 'test'])

if __name__ == '__main__':
    unittest.main()