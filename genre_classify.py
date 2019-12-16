"""@author: Yash Dani Student Id: 1001707349"""

import pandas as pd
import os, pickle, ast, operator
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from nltk.stem.porter import PorterStemmer

def get_results(query):
    global prior_probability, post_probability
    initialize()
    if os.path.isfile("classifierPicklePrior.pkl"):
        prior_probability = pickle.load(open('classifierPicklePrior.pkl', 'rb'))
        post_probability = pickle.load(open('classifierPicklePost.pkl', 'rb'))
    else:
        (prior_probability, post_probability) = build_and_save()
    return eval_result(query)

def eval_result(query):
    processed_query = pre_processing(query)
    sum=0
    genre_score = {}
    perc = []
    notrequiredlist={'Vision View Entertainment', 'Aniplex', 'GoHands', 'BROSTA TV', 'Rogue State','Carousel Productions', 'Odyssey Media', 'Sentai Filmworks', 'Pulser Productions', 'Mardock Scramble Production Committee', 'Telescene Film Group Productions', 'The Cartel' }
    for genre in prior_probability.keys():
        if genre in notrequiredlist:
            continue
        score = prior_probability[genre]
        for token in processed_query:
            if (genre, token) in post_probability.keys():
                score = score * post_probability[(genre, token)]
        genre_score[genre] = score
    sorted_score_map = sorted(genre_score.items(), key=operator.itemgetter(1), reverse=True)
    for i in sorted_score_map:
        sum += i[1]
    for i in range(len(sorted_score_map)):
        perc.append([sorted_score_map[i][0], sorted_score_map[i][1], (sorted_score_map[i][1] / sum) * 100])
    return perc, sorted_score_map
    # return sorted_score_map

def build_and_save():
    row_count = 0
    token_count = 0
    post_probability = {}
    token_genre_count_map = {}
    genre_count_map = {}
    for row in meta_data.itertuples():
        keywords = []
        genres = []
        for col in meta_cols.keys():
            col_values = getattr(row, col)
            parameters = meta_cols[col]
            # Paramter is None for tagline and overview columns, so appending data in keywords[]
            if parameters is None:
                keywords.append(col_values if isinstance(col_values, str) else "")
            else:
                col_values = ast.literal_eval(col_values if isinstance(col_values, str) else '[]')
                for col_value in col_values:
                    for param in parameters:
                        genres.append(col_value[param])

        tokens = pre_processing(' '.join(keywords))
        for genre in genres:
            if genre in genre_count_map:
                genre_count_map[genre] += 1
            else:
                genre_count_map[genre] = 1
            for token in tokens:
                token_count += 1
                if (genre, token) in token_genre_count_map:
                    token_genre_count_map[(genre, token)] += 1
                else:
                    token_genre_count_map[(genre, token)] = 1

        row_count += 1
    for (genre, token) in token_genre_count_map:
        post_probability[(genre, token)] = token_genre_count_map[(genre, token)] / token_count

    prior_probability = {x: genre_count_map[x]/row_count for x in genre_count_map}
    save(prior_probability, post_probability)
    return (prior_probability, post_probability)

def pre_processing(data_string):
    # for noise in noise_list:
    #     data_string = data_string.replace(noise, "")
    tokens = tokenizer.tokenize(data_string)
    processed_data = []
    for t in tokens:
        if t not in stopword:
            processed_data.append(stemmer.stem(t).lower())
    return processed_data

def save(prior_probability, post_probability):
    pickle.dump(prior_probability, open('classifierPicklePrior.pkl', 'wb+'))
    pickle.dump(post_probability, open('classifierPicklePost.pkl', 'wb+'))

def initialize():
    global meta_data, meta_cols, tokenizer, stopword, stemmer, meta_data, test_data
    # data Fetch
    # data_folder = 'data/'
    meta_cols = {"genres":['name'], "overview":None, "tagline":None}
    meta_data = pd.read_csv('movies_metadata.csv', usecols=meta_cols.keys())
    train_data, test_data = train_test_split(meta_data)
    # testAccuracy(test_data)
    # print(testAccuracy(test_data))
    tokenizer = RegexpTokenizer(r'[a-zA-Z0-9]+')
    stopword = stopwords.words('english')
stemmer = PorterStemmer()

def train_test_split(df, split=0.1):
    train_size = int((1-split)*len(df))
    return df[:train_size], df[train_size:]

def testAccuracy(test_data):
    num_correct_predictions = 0
    print(type(test_data), test_data)
    for index in list(test_data.index):
        y_result = test_data.at[index, 'genres']
        query = test_data.at[index, 'overview']
        y_predict = get_results(query)[:5]
        for genre in y_predict:
            if y_result == genre[0]:
                num_correct_predictions+=1
    accuracy = num_correct_predictions/len(test_data)
    return accuracy

# print(get_results(""))
