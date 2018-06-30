import json
import numpy as np
import re
from stop_words import get_stop_words
from pprint import pprint


def loading_file(filename):
    train_text = []
    train_id = []
    train_res = []

    with open(filename, encoding = "utf-8") as f:
        data = json.load(f)

    for each in data:
        train_text.append(each["text"])
        train_id.append(each["id"])
        train_res.append(each["sentiment"])

    i = 0
    stopwords = get_stop_words('russian')

    for each in train_text:
        train_text[i] = list(filter(None, re.sub("[^а-яА-Я]", " ", each).lower().split(' ')))
        train_text[i] = [w for w in train_text[i] if not w in stopwords]
        if(train_res[i] == "negative"):
            train_res[i] = 0
        elif(train_res[i] == "positive"):
            train_res[i] = 2
        else:
            train_res[i] = 1
        i+=1
    
    return train_id, train_text, train_res

