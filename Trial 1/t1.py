# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 09:54:27 2018

@author: kansa
"""
import nltk
from nltk.corpus import stopwords

sent=input("Enter the Sentence--").lower()
new_sent=""
for i in sent.split():
    val=i
    if not val in stopwords.words('english'):
        new_sent+=val + " "
print(new_sent)
