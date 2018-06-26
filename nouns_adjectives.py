# change
from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import nltk
# fp=open(r'text.txt','r',encoding="utf8")
# paragraph=fp.read()
# paragraph=paragraph.lower()
# fp.close()
# new_data = ""
# punctuations = ['.', ',', '/', '\\', '(', ')']
# for character in paragraph:
# 	if (character in punctuations):
# 		# new_data = new_data + '.'
# 		new_data = new_data + ' '
# 	else:
# 		new_data = new_data + character
# paragraph = new_data

# print(paragraph)

paragraph  = input("Enter a sentence")
paragraph = paragraph.lower()

sent_text=nltk.sent_tokenize(paragraph)
data=[]
from nltk.corpus import stopwords
for sentence in sent_text:
        tokenized_text = nltk.word_tokenize(sentence)
        sent_data=[w for w in tokenized_text if not w in stopwords.words('english')]
        data.extend((sent_data))
# print(type(data))

fadj = open('Anew.txt', 'r')
adjectives = fadj.read().split('\n')
# print(adjectives)
# print('\n\n\n\n')
fadj.close()
fnouns = open('Nnew#1.txt', 'r')
nouns = fnouns.read().split('\n')
# print(nouns)
fnouns.close()

prev_word = data[0]
check = 0
count = 0
curr_adj = ''
for word in data:
	if check == 0:
		check = 1
		if word in nouns:
			print(word)
		continue
	else:
		# check = 1
		if word in nouns:
			if prev_word in adjectives:
				print(prev_word, word)
				curr_adj = 'None'
			else:
				print(word)
		elif word in adjectives:
			curr_adj = word
		else:
			if curr_adj != 'None':
				print(curr_adj)
	prev_word = word
	count += 1
if curr_adj!= 'None':
	print(curr_adj)
print(" 				DONE\n\n")


# values = array(data)
# print(values)
# # integer encode
# label_encoder = LabelEncoder()
# integer_encoded = label_encoder.fit_transform(values)
# print(integer_encoded)
# print(values[list(integer_encoded).index(205)])
# # binary encode
# onehot_encoder = OneHotEncoder(sparse=False)
# integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
# print(integer_encoded)
# onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
# print(onehot_encoded)
# # invert first example
# inverted = label_encoder.inverse_transform([argmax(onehot_encoded[1])])
# print(inverted)

