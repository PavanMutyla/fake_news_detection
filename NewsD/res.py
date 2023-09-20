import pandas as p
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import re
import string
import numpy
def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) 
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)    
    return text

LS = joblib.load('C:\\Users\\PAVAN\\OneDrive\\Desktop\\New folder (2)\\DeleTeeee\\NewsD\\model.joblib')
vec = TfidfVectorizer()
def manual_testing(news):
    testing_news = {"text":[news]}
    new_def_test = p.DataFrame(testing_news)
    new_def_test["text"] = new_def_test["text"].apply(wordopt) 
    new_x_test = new_def_test["text"]
    new_xv_test = vec.fit_transform(new_x_test)
    p_lr = LS.predict(new_xv_test)
    return p_lr

data='RajnathSinghchairsSCOdefenceministersmeeting'

print(manual_testing(data))