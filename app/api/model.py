#! /usr/bin/python3

"""
Preditive model for predicting best strains to match input variables for
Med-Cab-2020
"""


# IMPORTS
import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import pickle
import en_core_web_sm
from spacy import load


df = pd.read_csv('Data/cannabis_new.csv')

nlp= en_core_web_sm.load()


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

filename = 'model.pkl'
# Open the file to save as pkl file
model_pkl = open(filename, 'wb')
pickle.dump(nn, model_pkl)
# Close the pickle instances
model_pkl.close()


def train(user_input):
    print('inside train()')
    model_pkl = open(filename, 'rb')
    nn2 = pickle.load(model_pkl)
    #nn2 = load('model.joblib')
    sample = [user_input]
    vec = model.transform(sample)
    dense = vec.todense()
    similar = nn2.kneighbors(dense, return_distance=False)
    similar.T

    output = []
    for i in range(5):
        elem = similar[0][i]
        output.append(elem)

    return output[0]
