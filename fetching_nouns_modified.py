

def chint(s):
    try:
        return type(int(s))==int
    except ValueError:
        return False
    
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import subprocess
import os
import random

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
fin = open('nouns_synid.txt', 'r')
count1 = 0
objects_id = dict()
while count1 < 55:
    line = fin.readline()
    id = line[:8]
    line = line[9:]
    line = line.split(',')
    for i in d:
        if i in line:
            print(i, "found with ID", id)
            if i not in objects_id:
                objects_id[i] = list()
                objects_id[i].append(id)
            else:
                objects_id[i].append(id)
    count1 += 1
print(objects_id)

fin.close()

for j in objects_id:
    PATH = "/Volumes/My Passport/Text to Image/textto3dscene/ShapeNetCore.v1"
    value = random.randint(0, len(objects_id[j])-1)
    PATH = PATH + '/' + objects_id[j][value] # can be changed
    print(objects_id[j][value])
    print(PATH)
    # os.system("cd" + PATH + '\n' + 'ls')
    directory = subprocess.check_output('ls', cwd = PATH)
    directory = str(directory)
    directory = directory[2:]
    directory = directory.split('\\n')
    value1 = random.randint(0, len(directory)-1)
    print(directory[value1])  #  can be changed
    PATH = "/Volumes/My\ Passport/Text\ to\ Image/textto3dscene/ShapeNetCore.v1"
    PATH = PATH + '/' + objects_id[j][value] # can be changed
    PATH = PATH + '/' + directory[value1] # can be changed
    # directory1 = subprocess.check_output('ls', cwd = PATH)
    # print(directory1)
    # subprocess.call('ls')
    os.system("cd " + PATH + '\n' + 'open model.obj')

