# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 09:54:27 2018

@author: kkansal
"""


def chint(s):
    try:
        return type(int(s))==int
    except ValueError:
        return False
    
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
fp=open("Nouns.txt",'r')
nouns=fp.read().split()
adj=fp.read().split()
sent=input("Enter the Sentence--").lower()
new_sent=""
for i in sent.split():
    val=i
    if not val in stopwords.words('english'):
        new_sent+=val + " "
l=new_sent.split()
lem=WordNetLemmatizer()
l=[lem.lemmatize(word) for word in l]
print(l)
d=dict()
count=0
z=[1]
while (count!=(len(l))):
    if not l[count] in nouns:
        if chint(l[count]):
            z[0]=int(l[count])
        else:
            z.append(l[count])
    if l[count] in nouns:
        print(z)
        if not l[count] in d:
            d[l[count]]=z
            print("done")
        else:
            d[l[count]][0] +=z[0]
            d[l[count]].extend(z[1:])
        z=[1]
    count+=1
print(d)
fp.close()

