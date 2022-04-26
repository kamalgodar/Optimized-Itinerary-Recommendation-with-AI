import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel

df = pd.read_csv('attractions_of_nepal_updated_columns.csv')
required_df = df.drop(columns = ['avg_rating', 'voted_by'])

tfv = TfidfVectorizer(min_df = 3, max_features = None, strip_accents = 'unicode',
                     analyzer = 'word', token_pattern = r'\w{1,}', 
                     ngram_range = (1,2),
                     stop_words = 'english')

tfv_matrix = tfv.fit_transform(required_df['genre'])
sig = sigmoid_kernel(tfv_matrix, tfv_matrix)
indices = pd.Series(required_df.index, index = required_df['title'])

def rec(title, sig = sig):
    idx = indices[title]
    sig_sco = list(enumerate(sig[idx]))
    sig_sco = sorted(sig_sco, key = lambda x:x[1], reverse = True)
    sig_sco = sig_sco[1:11]
    destination = [i[0] for i in sig_sco]
    series = required_df['title'].iloc[destination]
    return(series.to_list())


