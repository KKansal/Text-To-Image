# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:34:03 2018

@author: kansa
"""
ft=
fp=open("nouns_synid.txt","r")
line=fp.readline()
l=line.split(" ",maxsplit=1)
print(l)
d=dict()
d[l[0]]=l[1].split(',')
print(d)
