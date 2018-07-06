# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:34:03 2018

@author: kansa
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 09:54:27 2018

@author: kkansal
"""
import random
import subprocess
import os    
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def chint(s):
    try:
        return type(int(s))==int
    except ValueError:
        return False
    
    
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
fp=open("nouns_synid.txt","r")
dmaster=dict()
line=fp.readline()
while (line!=""):
    if(line!='\n'):
        l=line.split(" ",maxsplit=1)
        #print(l)
        dmaster[l[0]]=l[1].split(',')
    line=fp.readline()
#print(d)    
fp.close()
d_id=dict()
for j in d:
    d_id[j]=[]
    for i in dmaster:
        if j in dmaster[i]:
            d_id[j].append(i)
print(d_id)

d_selected=dict()
for k in d_id:
    d_selected[k]=random.choice(d_id[k])
    path='C:\\Users\\kansa\\Desktop\\TexttoImage\\textto3dscene\\ShapeNetCore.v1\\'  + d_selected[k]
    out=subprocess.run(['dir','/W'], stdout=subprocess.PIPE,shell=True,cwd=path).stdout.decode('utf-8')
    l=out.split('\n')
    ch=random.choice(l)
    ch=ch.split()
    ch=random.choice(ch)
    ch=ch[1:-1]
    print("Random ID-",ch)
    path=path +'\\'+ch
    out=subprocess.run(['mkdir',k],shell=True,cwd='C:\\Users\\kansa\\Documents\\GitHub\\Text-To-Image\\Keshav Programs\\Resources')
    out=subprocess.run(['xcopy',path,'/e'], stdout=subprocess.PIPE,shell=True,cwd='Resources\\'+k).stdout.decode('utf-8')
    print(out)
    
    





    
