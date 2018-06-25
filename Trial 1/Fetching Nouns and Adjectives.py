# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 09:54:27 2018

@author: kansa
"""
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
fp=open("Nouns.txt",'r')
ft=open("Adjectives.txt",'r')
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
i=0
count=0
while (count!=(len(l))):
    z=[]
    try:
        while not l[i] in nouns:
            try:
                l[i]=int(l[i])
            except ValueError:
                pass
            z.append(l[i])
            count+=1
            i+=1
            type(l[i])
#            print("adjective")   
        d[l[i]]=z
        i+=1
        count+=1
    except IndexError:
        print("ERROR-The sentence has an adjective without a NOUN")
print(d)
fp.close()
ft.close()
        
