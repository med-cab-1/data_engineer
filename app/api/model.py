#! /usr/bin/python3

"""
Preditive model for predicting best strains to match input variables for
Med-Cab-2020
"""


import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import pickle

from spacy import load
import en_core_web_sm
# nlp= en_core_web_sm.load()



# Define a function to tokenize the text:
# def tokenizer(text, nlp):
#     doc=nlp(text)
#     return [token.lemma_ for token in doc if ((token.is_stop == False) and
#     (token.is_punct == False)) and (token.pos_ != 'PRON')]


def train(user_input):
    df = pd.read_csv('Data/cannabis_new.csv')
    print('Before making nlp')
    print(user_input)
    nlp= en_core_web_sm.load()
    print('After making nlp')

    def tokenizer(text):
        doc=nlp(text)
        return [token.lemma_ for token in doc if ((token.is_stop == False) and
        (token.is_punct == False)) and (token.pos_ != 'PRON')]

    # Build the model:
    model = TfidfVectorizer(stop_words = 'english',
                           ngram_range = (1,2),
                           max_df = .95,
                           min_df = 3,
                           tokenizer = tokenizer)

    # Fit and transform the data:
    dtm = model.fit_transform(df['Effects'])

    # Get features:
    dtm = pd.DataFrame(dtm.todense(), columns = model.get_feature_names())

    nn = NearestNeighbors(n_neighbors=5, algorithm='kd_tree')
    nn.fit(dtm)

    # Fin similar strains and return the strain_id:
    # Victorise the text:
    sample = [user_input]
    vec = model.transform(sample)
    # find similar effects:
    dense = vec.todense()
    similar = nn.kneighbors(dense, return_distance=False)
    similar.T

    output = []
    for i in range(5):
        elem = similar[0][i]
        output.append(elem)


    return output[0]

    # result = df[(df['Id']==output[0]) |
    #         (df['Id']==output[1]) |
    #         (df['Id']==output[2]) |
    #         (df['Id']==output[3]) |
    #         (df['Id']==output[4]) ]
    # result = result.sort_values(by=['Rating'], ascending=False)
    #
    # print(result.head())
