# -*- coding: UTF-8 -*-
from nltk import ngrams
from nltk import FreqDist
from nltk.corpus import brown

import codecs
import operator
import sys
import nltk
import pandas as pd
import numpy as np 
import re

wordfile=codecs.open("saveFileName.txt",encoding="gbk")
num = 0
sentences = []
line = wordfile.readlines()
while len(line) != 0:
  sentences += line
  line = wordfile.readlines()
  num = num +1 

wordfile.close()
 
lenT = len(sentences)
for i in range(lenT):
    sentences[i] = sentences[i].split(".",1)[0]
for i in range(lenT):
    sentences[i] = sentences[i].split("BY",1)[0]
    sentences[i] = sentences[i].split("by",1)[0]
    t= sentences[i].split("《")
    if(len(t)==1):
        sentences[i] = t[0]
    else:
        sentences[i] = t[1]
    t1= sentences[i].split("》")
    if(len(t1)==1):
        sentences[i] = t1[0]
    else:
        sentences[i] = t1[0]

    #print(sentences[i])
fd= nltk.FreqDist(sentences)
 
for key in fd:
    if(fd[key]>1):
        print(key, fd[key])


#for i in range(lenT):
#   sentences[i] = sentences[i].split("[",1)[0]
#for i in range(lenT):
#   sentences[i] = sentences[i].split("[",1)[0]
  