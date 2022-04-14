#!/usr/bin/python

import sys

f = open(sys.argv[1],'r')
n = int(sys.argv[2])

lines = f.readlines()
lines = [line.strip() for line in lines]

dict={}

i=0
for x in range(n):
    string = lines[i]
    word = string.split()
    x=word[0]
    count=int(word[1])

    dict[x]=count
    i+=1

sdict = sorted(dict.items(), key = lambda item: item[1], reverse = True)

