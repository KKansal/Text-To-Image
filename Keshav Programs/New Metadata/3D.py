#import random
import subprocess
#import os    
#import nltk
from nltk.corpus import stopwords,wordnet
import operator
from nltk.stem import WordNetLemmatizer
import pickle
#import functools
import math
def ch_int(s):
    try:
        return type(int(s))==int
    except ValueError:
        return False
    
def formdict(nouns,l):
    d=dict()
    count=0
    z=[1]
    while (count!=(len(l))):
        if not l[count] in nouns:
            if ch_int(l[count]):
                z[0]=int(l[count])
            else:
                z.append(l[count])
        if l[count] in nouns:
#            print(z)
            if not l[count] in d:
                d[l[count]]=z
#                print("done")
            else:
                d[l[count]][0] +=z[0]
                d[l[count]].extend(z[1:])
            z=[1]
        count+=1
    return d


def formnouns(d_data):
    nouns=[]
    for i in d_data:
        nouns.extend(d_data[i]['cat'])
    print('nouns',len(nouns))
    return nouns

def seltest1(d_objects,d_data):
    l_seltest1=dict()
    for i in d_objects:
        l_seltest1[i]=[]
        for j in d_data:
            if i in d_data[j]['cat']:
                l_seltest1[i].append(j)
    return(l_seltest1)

def sel(d):
    sorted_d=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
    return sorted_d


def sel_lemma(sel_val):
    k=max(sel_val,key=operator.itemgetter(1))[1]
#    print(k)
    new_sel_val=[]
    for i in sel_val:
        if i[1]*10>=math.floor(k*10):
            new_sel_val.append(i)
    return(new_sel_val)
def compare(it_desc,param,l,d_data):
    #l=list of matching id
    #param=tag,lemma,name
    #desc=Adjectives of that element of d
    t_score_d=dict()
    syn_it_desc=list(map(lambda x : wordnet.synsets(x)[0],it_desc[1:]))
#    print(syn_it_desc)
    for i in l:
        id_desc=d_data[i][param]
        syn_id_desc=[]
        for word in id_desc:
            try:
                syn_id_desc.append(wordnet.synsets(word)[0])
            except IndexError:
                pass
#        print(syn_id_desc)
        t_score=0
        if len(syn_id_desc)!=0:
            for j in syn_id_desc:
                for k in syn_it_desc:
                    try:
                        t_score+=j.wup_similarity(k)/len(syn_id_desc)
                    except TypeError:
                        t_score+=0
        else:
            t_score=0
        t_score_d[i]=t_score
    return t_score_d
        
    
#def main():
fp=open("data2.dat",'rb')
d_data=pickle.load(fp)
fp.close()
sent=input("Enter the Sentence--").lower().split()
new_sent=""
for word in sent:
    if not word in stopwords.words("english"):
        new_sent+=word + " " 
l=new_sent.split()
lem=WordNetLemmatizer()
l=[lem.lemmatize(word) for word in l]
print(l)
d=formdict(formnouns(d_data),l)
print(d)
match_id=seltest1(d,d_data)
#print(match_id)
ft=open("selected.txt","w")
for i in match_id:
    k1=compare(d[i],'lemma',match_id[i],d_data)
    sel1=sel_lemma(sel(k1))
    sel_matchid=[]
    for j in sel1:
        sel_matchid.append(j[0])
    sel2=sel(compare(d[i],'tag',sel_matchid,d_data))
    print(sel2)
    selected_id=max(sel2,key=operator.itemgetter(1))[0]
    ft.writelines(selected_id.lstrip('wss.')+'\n')
ft.close()
out=subprocess.check_output(['blender','--python','3D_2.py'],shell=True)
print(out)
#subprocess.call(['blender','--background','--python','3d_2.py'])

# ID NOW HAS BEEN SELECTED
   # output=
    
    
    
    
    
    
    
    
    
#    print(seltest1(d,d_data))
# main()

"""
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
"""    
    





    
