# change
from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import nltk
fp=open(r'text.txt','r',encoding="utf8")
paragraph=fp.read()
paragraph=paragraph.lower()
fp.close()
new_data = ""
punctuations = ['.', ',', '/', '\\', '(', ')']
for character in paragraph:
	if (character in punctuations):
		# new_data = new_data + '.'
		new_data = new_data + ' '
	else:
		new_data = new_data + character
paragraph = new_data



sent_text=nltk.sent_tokenize(paragraph)
data=[]
from nltk.corpus import stopwords
for sentence in sent_text:
        tokenized_text = nltk.word_tokenize(sentence)
        sent_data=[w for w in tokenized_text if not w in stopwords.words('english')]
        data.extend((sent_data))
#print(data)


values = array(data)
print(values)
# integer encode
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(values)
print(integer_encoded)
# binary encode
onehot_encoder = OneHotEncoder(sparse=False)
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
print(onehot_encoded)
# invert first example
inverted = label_encoder.inverse_transform([argmax(onehot_encoded[0, :])])
print(inverted)

