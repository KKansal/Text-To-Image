# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 11:59:27 2018

@author: kansa
"""
import pickle
fp=open("data.dat",'rb')
d=pickle.load(fp)
print(d)
print(type(d))