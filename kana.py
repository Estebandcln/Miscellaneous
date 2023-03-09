# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:47:39 2020

@author: DECLINE
"""


import time
import random as rd

m=[]
n=[]
lv=['a','i','u','e','o']
lc=['k','g','s','z','t','d','n','h','b','p','m','y','r','w']
k=['katakana','hiragana']
for i in lv:
    for j in lc:
        m.append(j)
        m.append(i)
        a=''.join(m)
        n.append(a)
        m=[]
for i in range(len(n)):
    if n[i]=='ti':
        n[i]='chi'
    elif n[i]=='tu':
        n[i]='tsu'
    elif n[i]=='si':
        n[i]='shi'
    elif n[i]=='zi':
        n[i]='ji'
    elif n[i]=='yi':
        n[i]='a'
    elif n[i]=='wi':
        n[i]='o'
    elif n[i]=='ye':
        n[i]='e'
    elif n[i]=='wu':
        n[i]='u'
    elif n[i]=='di':
        n[i]='i'
    elif n[i]=='hu':
        n[i]='fu'
    elif n[i]=='du':
        n[i]='n'
n.remove('we')
"""print(n)"""
for i in range(20):
    if i==0:
        print(rd.choice(k),',',rd.choice(n))
    else:
        time.sleep(5)
        print(rd.choice(k),',',rd.choice(n))
print('fin')
