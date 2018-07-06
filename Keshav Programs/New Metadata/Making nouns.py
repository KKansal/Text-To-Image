l=[]
dt=[]
import pickle
from nltk.stem import WordNetLemmatizer 
with open("created_database_category2.txt",'r') as fp:
        data_cat=fp.readlines()
with open("created_database_lemmas2.txt",'r') as fp:
        data_lemma=fp.readlines()
with open("created_database_names2.txt",'r') as fp:
        data_name=fp.readlines()
with open("created_database_tags2.txt",'r') as fp:
        data_tag=fp.readlines()

data_cat=list(map(lambda x: x.split('\t'),data_cat))
data_lemma=list(map(lambda x: x.split('\t'),data_lemma))
data_name=list(map(lambda x: x.split('\t'),data_name))
data_tag=list(map(lambda x: x.split('\t'),data_tag))
print(data_cat)
d_data=dict()
lemmatizer=WordNetLemmatizer()
for pair in data_cat:
    cat=pair[1].rstrip('\n').split(",")
    cat=[lemmatizer.lemmatize(i) for i in cat]
    d_data[pair[0]]={"cat":cat}

for pair in data_lemma:
    lemma=pair[1].rstrip('\n').split(",")
    lemma=[lemmatizer.lemmatize(i) for i in lemma]
    try:
        d_data[pair[0]]["lemma"]=lemma
    except KeyError:
        l.append(pair[0])    

for pair in data_name:
    lemma=pair[1].rstrip('\n').split(",")
    lemma=[lemmatizer.lemmatize(i) for i in lemma]
    try:
        d_data[pair[0]]["name"]=lemma
    except KeyError:
        l.append(pair[0])    
#print(d_data)    

#print(data_tag)
for pair in data_tag:
    try:
        lemma=pair[1].rstrip('\n').split(",")
        lemma2=[]
        for i in range(len(lemma)):
            lemma2.extend(lemma[i].split())  
        lemma2=[lemmatizer.lemmatize(i) for i in lemma2]
        try:
            d_data[pair[0]]["tag"]=lemma2   
        except KeyError:
            l.append(pair[0])
    except IndexError:
        dt.append(pair)
        
print(d_data)    

fp=open("data2.dat",'wb')
pickle.dump(d_data,fp)
fp.close()
print(d_data)
"""
nouns=set()
for i in range(len(data)):
    data[i]=data[i].split('\t')
    cat=data[i][1]
    cat=cat.rstrip('\n')
    print(cat)
    cat=cat.split(",")
    for j in cat:
        nouns.add(j)
ft=open("Nouns.txt",'w')
for k in nouns:
    ft.write(k.lower() +',')
ft.close()
"""
