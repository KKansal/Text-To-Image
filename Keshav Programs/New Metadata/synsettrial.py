# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 13:32:27 2018

@author: kansa
"""

import nltk
from nltk.corpus import wordnet
w1=wordnet.synsets("black")
w2=wordnet.synsets("baleful")
print(w2)
print(w1[0].shortest_path_distance(w2[0]))

#lch_similarity
#lin_similarity
#path_similarity
#res_similarity
#shortest_path_distance
#wup_similarity
